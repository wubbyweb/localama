import gradio as gr
import os
import shutil



def upload_file(file):
        # Define the project location for file uploads
    PROJECT_DIR = "./doc"

    # Ensure the project directory exists
    os.makedirs(PROJECT_DIR, exist_ok=True)

    if file is not None:
        file_path = os.path.join(PROJECT_DIR, file.name)
        print(file_path)
        base_name = os.path.basename(file.name)
        shutil.copy(file.name, "./doc/"+base_name)
        return f"File uploaded successfully to {file_path}"
    return "No file was uploaded"

def process_simple_query(input_text, query):
    # This is a placeholder function. Replace with actual processing logic.
    return f"Response to '{query}' based on input: {input_text}"

def process_elongated_query(elongated_input, query):
    # This is a placeholder function. Replace with actual processing logic.
    return f"Detailed response to '{query}' based on elongated input: {elongated_input[:50]}..."

with gr.Blocks() as demo:
    gr.Markdown("# Multi-Component Gradio Interface")
    
    with gr.Row():
        # Container 1: File Upload
        with gr.Column():
            file_input = gr.File(label="Upload File")
            upload_output = gr.Textbox(label="Upload Status")
            file_input.upload(fn=upload_file, inputs=[file_input], outputs=[upload_output])

    with gr.Row():
        # Container 2: Simple Query
        with gr.Column():
            input_text = gr.Textbox(label="Input Text")
            query_text = gr.Textbox(label="Query")
            submit_btn = gr.Button("Submit Query")
            response_text = gr.Chatbot()
            
            submit_btn.click(
                fn=process_simple_query,
                inputs=[input_text, query_text],
                outputs=[response_text]
            )

    with gr.Row():
        # Container 3: Elongated Query
        with gr.Column():
            elongated_input = gr.Textbox(label="Elongated Input", lines=5)
            elongated_query = gr.Textbox(label="Query")
            elongated_submit_btn = gr.Button("Submit Elongated Query")
            elongated_response = gr.Chatbot()
            
            elongated_submit_btn.click(
                fn=process_elongated_query,
                inputs=[elongated_input, elongated_query],
                outputs=[elongated_response]
            )

demo.launch()