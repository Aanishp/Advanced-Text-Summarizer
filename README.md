# 🧠 Advanced Text Summarizer & Multilingual Translator
This project is a powerful and intuitive web application for text summarization and translation. Built with Streamlit and leveraging the Hugging Face Transformers library, it allows users to condense long articles, documents, or paragraphs into concise summaries. It supports both manual text input and file uploads (PDF, TXT) and offers multilingual translation for the generated summaries.

The application is built entirely in Python, using the facebook/bart-large-cnn model for high-quality abstractive summarization and Google Translate for language support.

---

## ✨ **Features**
- **High-Quality Summarization:** Utilizes the powerful BART model from Hugging Face to generate accurate and coherent summaries.
- Multiple Input Methods:
  - 📝 **Manual Text:** Directly paste text into a text area.
  - 📄 **File Upload:** Supports .pdf and .txt files for easy document processing.
- **Multilingual Support:** Translate the final summary into several languages, including Hindi, Kannada, Spanish, French, and German.
- **Chunking for Long Texts:** Automatically handles texts longer than the model's token limit by splitting, summarizing, and rejoining them.
- **Downloadable Output:** Easily download the generated summary as a .txt file.
- **User-Friendly Interface:** A clean, responsive, and easy-to-navigate UI built with Streamlit.

---

## 💻 **Tech Stack**
- **Web Framework:** Streamlit
- **ML/AI:** Hugging Face Transformers, PyTorch
- **Summarization Model:** BART (bart-large-cnn)
- **PDF Processing:** PyPDF2
- **Translation:** googletrans

---

## 🚀 **Getting Started**
Follow these instructions to set up and run the project locally.
### **Prerequisites**
- Python 3.7+

### 🔹 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Aanishp/Advanced-Text-Summarizer.git
cd Advanced-Text-Summarizer
```

### 🔹 2️⃣ Set Up a Virtual Environment It's highly recommended to use a virtual environment.
```bash
# Create and activate the environment
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate # On macOS/Linux
```

### 🔹 3️⃣ Install Dependencies Install all the required packages from the requirements.txt file.
```bash
pip install -r requirements.txt
```

### 🔹 4️⃣ Run the Application
Execute the main script using the Streamlit CLI to start the application.
```bash
streamlit run main.py
```

### 🔹 5️⃣ Access the Application Open your web browser and navigate to:
```bash
http://localhost:8501
```

---

## 👥 Team Members  
🚀 [Aanish P](https://github.com/Aanishp)  
🚀[M.S.Prajwal](https://github.com/prajwal50)  
🚀 [](https://github.com/VamshiNandhanReddy)  
🚀 []()  

📍 **Department of Artificial Intelligence & Machine Learning**  
📍 **BMS Institute of Technology & Management, Bengaluru** 

---
