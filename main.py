from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import gradio as gr

# Load GPT-J model and tokenizer from Hugging Face
model_name = "EleutherAI/gpt-j-6B"  # GPT-J 6B model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

# Create a text-generation pipeline using GPT-J
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Function to generate an academic outline
def generate_outline(topic):
    """
    Generate a detailed academic outline for the given topic.
    """
    prompt = f"""
    Write a detailed academic paper outline on the topic: "{topic}".
    The outline should include the following sections:
    - Introduction (background, problem statement, objectives)
    - Literature Review (summary of key studies)
    - Methodology (approach, tools, and methods)
    - Results (expected findings or actual results)
    - Discussion (interpretation and significance of results)
    - Conclusion (summary, implications, and future directions)
    """
    result = generator(prompt, max_length=300, num_return_sequences=1, temperature=0.7)
    return result[0]["generated_text"]

# Function to expand a section of the outline
def expand_section(section, topic):
    """
    Generate a draft for a specific section of the academic paper.
    """
    prompt = f"""
    Write a detailed draft for the "{section}" section of an academic paper on "{topic}".
    Use formal academic language and include placeholder citations (e.g., (Author, Year)).
    """
    result = generator(prompt, max_length=400, num_return_sequences=1, temperature=0.7)
    return result[0]["generated_text"]

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Free AI Academic Writing Copilot (Powered by GPT-J)")
    
    topic_input = gr.Textbox(label="Enter your research topic:")
    outline_button = gr.Button("Generate Outline")
    outline_output = gr.Textbox(label="Generated Outline", lines=15)
    
    section_input = gr.Textbox(label="Enter the outline section to expand (e.g., 'Introduction'):")
    expand_button = gr.Button("Expand Section")
    section_output = gr.Textbox(label="Generated Section Draft", lines=15)
    
    outline_button.click(fn=generate_outline, inputs=topic_input, outputs=outline_output)
    expand_button.click(fn=expand_section, inputs=[section_input, topic_input], outputs=section_output)

demo.launch()
