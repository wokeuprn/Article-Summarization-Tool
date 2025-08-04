📝 Article Summarizer using NLP

This is a simple and interactive Article Summarizer Web App developed as part of an AI internship project. It leverages NLP (Natural Language Processing) techniques to summarize long texts using a transformer-based model. Built with Streamlit and Hugging Face Transformers, the app lets users paste large paragraphs or articles and returns a well-formed summary in seconds.
Whether you're condensing blog posts, academic papers, or lengthy notes, this tool helps extract key information quickly and efficiently.

🔧 Features
    ✅ Clean and beginner-friendly Streamlit interface
    ✅ Abstractive summarization using facebook/bart-large-cnn mode
    ✅ Handles long text inputs (up to 10,000 words)
    ✅ Real-time output with loading spinner and success indicator
    ✅ Caches the model for faster performance on repeated use

🧠 Technologies Used
    Python 3.9+
    Streamlit – for building the frontend
    Hugging Face Transformers – for loading the pretrained summarization model
    facebook/bart-large-cnn – state-of-the-art abstractive summarization model


🚀 How to Run
1) Clone the repository
              git clone https://github.com/your-username/your-repo-name.git cd your-repo-name

2) Install dependencies
               pip install -r requirements.txt

3) Run the app
               streamlit run (absolute path of the python file)  
