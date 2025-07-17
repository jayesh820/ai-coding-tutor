import gradio as gr
from openai import OpenAI
topic_to_subtopics = [
    "Python",
    "JavaScript",
    "Java",
    "C++",
    "C#",
    "Ruby",
    "Go (Golang)",
    "Swift",
    "PHP",
    "Rust"
]
subtopic_content = [
    "Variables and Data Types",
    "Syntax and Semantics",
    "Operators",
    "Input and Output",
    "Comments",
    "Conditional Statements",
    "Loops and Loop Control Statements",
    "Functions /Method ",
    "Data Structures",
    "Object-Oriented Programming (OOP)",
    "File Handling",
    " Error Handling"
]
google_gemini_key="Enter your google gemini api key"
mod =OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/",api_key=google_gemini_key)
def google_geminia(language_name,language_topic,other_question):
    masaage=[
        {"role":"system","content":f"You are a programming teacher. Explain the topic '{language_topic}' in the context of '{language_name}'. When a user asks a question, relate the answer to the selected language and topic. Provide a structured answer with examples. and also explain the each topics in just 2 to 3 lines and each line is seperated by new line "},
        {"role":"user","content": f"Relate the topic '{language_topic}' with the programming language '{language_name}', and answer this question: {other_question}. Give structured output, explanation, and code samples if needed." }
    ]
    output=  mod.chat.completions.create(
    messages=masaage,
    model="gemini-1.5-flash"
    )
    print(f"Language: {language_name}")
    print(f"Topic: {language_topic}")
    print(f"Question: {other_question}")
    return output.choices[0].message.content

with gr.Blocks(theme=gr.themes.Soft(), title="Programmer Teacher Q&A") as demo:
    gr.Markdown("""
    <h1 style='text-align: center; color: #4a90e2;'>👨‍🏫 Fluent Teacher</h1>
    <p style='text-align: center;'>Select a programming language and ask your question. I will try my best to answer it!</p>
    """)

    with gr.Row():
        lang_dropdown = gr.Dropdown(label="Select Programming Language", choices=list(topic_to_subtopics))
    with gr.Row():    
        lang_dropdown1 = gr.Dropdown(label="Select Topics", choices=list(subtopic_content))
    with gr.Row():
        user_question = gr.Textbox(label="Type your question here")
    with gr.Row():
        answer_box = gr.Textbox(label="Answer", lines=10,interactive=False)
    submit_btn = gr.Button("Get Answer 💡")
    submit_btn.click(fn=google_geminia, 
                     inputs=[lang_dropdown,lang_dropdown1, user_question], 
                     outputs=answer_box
                    )

demo.launch()
    