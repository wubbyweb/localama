def process_txt_file(file_path: str) -> List[str]:
    """
    Process a text file and return its contents as a list of strings.

    Args:
        file_path (str): The path to the text file.

    Returns:
        List[str]: A list of strings, each representing a line in the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().splitlines()
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return []