# Gradio Chatbot with Chroma Database

This repository contains a simple Gradio-based chatbot application that uses a Chroma database for text retrieval. The workflow includes creating a Chroma database from markdown files, then using the database to provide relevant responses in the chatbot interface.

![Chatbot Animation](https://raw.githubusercontent.com/Aman-Khokhar18/AWS_Chatbot/main/Images/Animation.gif)


## Features

1. **Chatbot with Gradio**  
   - `app.py` provides a straightforward Gradio chatbot interface.
   - Integrates with OpenAI’s GPT models for generating responses.

2. **Create Chroma Database**  
   - `create_database.py` handles the creation of a Chroma database from a set of local markdown files.
   - Useful for storing and retrieving information in an efficient manner.

3. **Extract Markdown from PDF**  
   - `utils_markdown_extract.py` offers a utility function to convert PDF files into markdown format, making it simpler to process your own custom text data.

4. **API Key Configuration**  
   - `environment.env` is used to store your OpenAI API key. Make sure to replace the placeholder with your actual key before running the chatbot.

5. **Dependencies**  
   - `requirements.txt` lists all the Python libraries needed to run the app. Install them using:
     ```bash
     pip install -r requirements.txt
     ```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- A valid OpenAI API key

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aman-Khokhar18/AWS_Chatbot
   cd AWS ChatBot
