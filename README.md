# 🎥 AI Video Assistant

<p align="center">
  <img src="screenshots/home.png" alt="AI Video Assistant" width="100%">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-RAG-success?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-blueviolet?style=for-the-badge)
![Mistral AI](https://img.shields.io/badge/Mistral-AI-orange?style=for-the-badge)

</p>

<p align="center">
An AI-powered platform that converts videos into searchable knowledge using Speech Recognition, Retrieval-Augmented Generation (RAG), and Large Language Models.
</p>

---

# 🚀 Live Demo

### 🌐 Streamlit App

https://ai-video-assistant-3ij66ujqcxluej77pcu3xj.streamlit.app/

---

# 📂 GitHub Repository

https://github.com/Muskan136/AI-Video-Assistant

---

# 📖 Overview

AI Video Assistant is an intelligent web application designed to analyze YouTube videos and uploaded audio/video files using Artificial Intelligence.

The application automatically extracts audio, generates speech transcripts, creates semantic embeddings, stores them inside a vector database, and allows users to interact with the content using Retrieval-Augmented Generation (RAG).

Instead of watching long videos again and again, users can simply ask questions about the video and instantly receive accurate AI-generated answers.

---

# ✨ Features

- 🎥 Analyze YouTube Videos
- 📂 Upload Local Audio & Video Files
- 🎙️ AI Speech Transcription
- 📑 Automatic Video Summarization
- 💬 AI Chat with Video Content
- 🔍 Semantic Search
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ Fast Vector Search using ChromaDB
- 🌐 Beautiful Streamlit Dashboard

---

# 🏗️ System Architecture

```
                 User
                   │
                   ▼
     Upload Video / YouTube URL
                   │
                   ▼
          Audio Extraction
                   │
                   ▼
      Speech-to-Text Transcription
                   │
                   ▼
          Transcript Chunking
                   │
                   ▼
 Sentence Transformer Embeddings
                   │
                   ▼
              ChromaDB
                   │
                   ▼
         LangChain Retriever
                   │
                   ▼
          Mistral AI Language Model
                   │
                   ▼
     AI-powered Question Answering
```

---

# 🛠 Tech Stack

### Programming Language

- Python

### Frontend

- Streamlit

### Artificial Intelligence

- LangChain
- Mistral AI
- Sentence Transformers

### Vector Database

- ChromaDB

### Audio Processing

- FFmpeg
- yt-dlp

### Libraries

- NumPy
- Requests
- ReportLab

---

# 📂 Project Structure

```
AI-Video-Assistant

│── app.py
│── requirements.txt
│── runtime.txt
│── README.md
│
├── core
│   ├── rag_engine.py
│   ├── vector_store.py
│   ├── summarizer.py
│   ├── transcriber.py
│
├── utils
│   └── audio_processor.py
│
├── downloads
│
├── chroma_db
│
└── screenshots
    └── home.png
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Muskan136/AI-Video-Assistant.git
```

Go to the project directory

```bash
cd AI-Video-Assistant
```

Create a virtual environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file inside the project directory.

```env
MISTRAL_API_KEY=YOUR_API_KEY
SARVAM_API_KEY=YOUR_API_KEY
SARVAM_STT_MODEL=saaras:v2.5
```

---

# ▶ Run the Application

```bash
streamlit run app.py
```

The application will be available at

```
http://localhost:8501
```

---

# 🔄 Workflow

1. Paste a YouTube URL or upload an audio/video file.
2. Extract audio automatically.
3. Generate speech transcripts.
4. Split transcript into semantic chunks.
5. Generate embeddings using Sentence Transformers.
6. Store embeddings in ChromaDB.
7. Retrieve relevant information using LangChain.
8. Generate intelligent answers using Mistral AI.

---

# 💡 Applications

- Meeting Intelligence
- Lecture Notes Generator
- Educational Video Assistant
- Interview Analysis
- Podcast Summarization
- Business Meeting Assistant
- Knowledge Retrieval

---

# 🚀 Future Enhancements

- Speaker Diarization
- Timestamp-based Answers
- Multi-language Support
- PDF Export
- Chat History
- Cloud Storage
- OCR from Video Frames

---

# 👩‍💻 Developed By

## **Muskan Sondhiya**

**B.Tech – Computer Science (Data Science)**

Artificial Intelligence • Machine Learning • Data Science • Generative AI

### GitHub

https://github.com/Muskan136

---

# 📬 Contact

If you'd like to collaborate, discuss AI projects, or provide feedback, feel free to connect through GitHub.

---

# ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.

It helps support future development and encourages open-source contributions.

---
