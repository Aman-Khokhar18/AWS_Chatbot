import pathlib
import pymupdf4llm 
import os

def convert_pdf_to_markdown(pdf_path, markdown_path):
    try:
        md_text = pymupdf4llm.to_markdown(pdf_path)
        markdown_file = pathlib.Path(markdown_path)
        markdown_file.parent.mkdir(parents=True, exist_ok=True)        
        markdown_file.write_text(md_text, encoding='utf-8')        
        print(f"Successfully converted '{pdf_path}' to '{markdown_path}'.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    pdf_directory = r"C:\Users\amank\AWS RAG Project\AWS Documentation\PDFs"
    markdown_directory = r"C:\Users\amank\AWS RAG Project\AWS Documentation\Markdown"

    if os.path.exists(pdf_directory):
        for filename in os.listdir(pdf_directory):
            if filename.lower().endswith('.pdf'):
                pdf_path = os.path.join(pdf_directory,filename)
                markdown_filename = os.path.splitext(filename)[0] + '.md'
                markdown_path = os.path.join(markdown_directory, markdown_filename)
                convert_pdf_to_markdown(pdf_path,markdown_path)
