import os
from typing import List, Tuple
from textProcessor import process_txt_file
from doc_processor import process_doc_file
from docx_processor import process_docx_file
from pdf_processor import process_pdf_file
from onenote_processor import process_onenote_file

def readfile(directory_path: str) -> List[Tuple[str, List[str]]]:
    """
    Process all files in the given directory and return a list of tuples
    containing file names and their contents as lists of strings.

    Args:
        directory_path (str): The path to the directory containing files to process.

    Returns:
        List[Tuple[str, List[str]]]: A list of tuples, each containing a file name
        and a list of strings representing the file's contents.
    """
    if not os.path.isdir(directory_path):
        raise ValueError(f"The provided path '{directory_path}' is not a directory or does not exist.")

    result = []

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension.lower()

            content = []
            if file_extension == '.txt':
                content = process_txt_file(file_path)
            elif file_extension == '.doc':
                content = process_doc_file(file_path)
            elif file_extension == '.docx':
                content = process_docx_file(file_path)
            elif file_extension == '.pdf':
                content = process_pdf_file(file_path)
            elif file_extension in ['.one', '.onetoc2']:  # Common OneNote file extensions
                content = process_onenote_file(file_path)

            if content:
                result.append((filename, content))

    return result

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python readfile.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        processed_files = readfile(directory_path)
        for filename, content in processed_files:
            print(f"File: {filename}")
            print(f"Content (first 3 lines): {content[:3]}")
            print("---")