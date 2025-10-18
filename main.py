import streamlit as st
from transformers import BartTokenizer, BartForConditionalGeneration
from PyPDF2 import PdfReader
from googletrans import Translator
import textwrap
import io

# Load BART summarization model
@st.cache_resource
def load_model():
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    return tokenizer, model

# Load Google Translate
@st.cache_resource
def load_translator():
    return Translator()

# Summarization logic
def summarize(text, tokenizer, model, max_length=130, min_length=30, do_sample=False):
    # Split long text into chunks under 1024 tokens
    sentences = text.split('. ')
    chunks = []
    current_chunk = ''

    for sentence in sentences:
        if len(tokenizer.encode(current_chunk + sentence, truncation=False)) < 1024:
            current_chunk += sentence + '. '
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + '. '
    if current_chunk:
        chunks.append(current_chunk.strip())

    # Summarize each chunk and combine
    summaries = []
    for chunk in chunks:
        inputs = tokenizer(chunk, return_tensors='pt', max_length=1024, truncation=True)
        summary_ids = model.generate(
            inputs['input_ids'],
            num_beams=4,
            length_penalty=2.0,
            max_length=max_length,
            min_length=min_length,
            early_stopping=True
        )
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True).strip()
        summaries.append(summary)

    return ' '.join(summaries)


# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf = PdfReader(pdf_file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""
    return text

# Translation logic
def translate_text(text, target_lang):
    try:
        translator = load_translator()
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        st.warning(f"⚠️ Translation failed: {e}")
        return text

# Main Streamlit app
def main():
    st.set_page_config(page_title="🧠 Advanced Text Summarizer", layout="centered")
    st.title("🧠 Advanced Text Summarizer with Multilingual Support")
    st.markdown("Enter or upload text, get a summary, translate it, and download the result.")

    # Sidebar for language and reset
    st.sidebar.header("🌍 Language & Options")
    language = st.sidebar.selectbox("Translate Summary To:", ["None", "English", "Hindi", "Kannada", "Spanish", "French", "German"], key='lang_choice')
    translate_codes = {
    "None": None,
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Spanish": "es",
    "French": "fr",
    "German": "de"
}

    # Reset all fields
    if st.sidebar.button("🔁 Reset All"):
        keys_to_clear = ["manual_input", "file_input", "lang_choice"]
        for key in keys_to_clear:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

    # Input method selection
    input_method = st.radio("Choose input method:", ["📝 Manual Text", "📄 Upload File"])
    input_text = ""

    if input_method == "📝 Manual Text":
        input_text = st.text_area("Enter your text here:", height=300, placeholder="Paste your long paragraph or article...", key="manual_input")

    elif input_method == "📄 Upload File":
        uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"], key="file_input")
        if uploaded_file:
            if uploaded_file.type == "application/pdf":
                input_text = extract_text_from_pdf(uploaded_file)
            else:
                input_text = uploaded_file.read().decode("utf-8")

    # Summarize and show output
    if st.button("✨ Summarize"):
        if not input_text.strip():
            st.warning("⚠️ Please enter or upload some text first.")
        else:
            with st.spinner("Generating summary..."):
                tokenizer, model = load_model()
                summary = summarize(input_text, tokenizer, model, max_length=100, min_length=20)

                if translate_codes[language] is not None:
                    summary = translate_text(summary, translate_codes[language])

                st.subheader("📝 Summary:")
                st.success(summary)

                # Expandable original input
                with st.expander("🔍 Original Text"):
                    st.write(textwrap.fill(input_text, width=100))

                # Download .txt file
                download_buffer = io.StringIO()
                download_buffer.write(summary)
                st.download_button(
                    label="📥 Download Summary as .txt",
                    data=download_buffer.getvalue(),
                    file_name="summary.txt",
                    mime="text/plain"
                )

if __name__ == "__main__":
    main()
