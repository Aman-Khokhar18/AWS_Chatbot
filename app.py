import gradio as gr
from query_chroma_database import query_chroma

def chat_with_chroma(user_message, chat_history):
    history_str = ""
    for user_msg, assistant_msg in chat_history:
        history_str += f"User: {user_msg}\nAssistant: {assistant_msg}\n"

    # Query the Chroma vector store
    response = query_chroma(query_text=user_message, history=history_str)

    if not response:
        response = "Sorry, I couldn't find any relevant information."

    chat_history.append((user_message, response))
    return chat_history, chat_history


with gr.Blocks() as demo:
    gr.Markdown("# AWS Documentation Chatbot")
    chatbot = gr.Chatbot()
    state = gr.State([])

    user_input = gr.Textbox(
        show_label=False,
        placeholder="Type in your query...",
        lines=1
    )
    
    user_input.submit(
        fn=chat_with_chroma,
        inputs=[user_input, state],
        outputs=[chatbot, state]
    )

demo.launch(share=True)
