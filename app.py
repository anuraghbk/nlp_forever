import gradio as gr
from keybert import KeyBERT

kw_model = KeyBERT()

# Define function for keyword extraction
def extract_keywords(text):
    #keywords = kw_model.extract_keywords(text)
    keywords=[i[0] for i in kw_model.extract_keywords(text,  keyphrase_ngram_range=(1,2)) ]
    return keywords

# Create Gradio interface
# Create Gradio interface
text_input = gr.Textbox(lines=5, label="Enter your text here")
output_text = gr.Textbox(label="Key themes")

custom_css = """
.gradio {
    background-color: #ffffff; /* White background */
    color: #000000; /* Black text color */
}
.gradio textarea, .gradio input[type="text"] {
    background-color: #f0f0f0; /* Light gray input background */
    color: #000000; /* Black text color */
    border: 1px solid #3498db; /* Blue border */
}
.gradio table {
    border: 1px solid #3498db; /* Blue border for tables */
}
"""

gr.Interface(
    fn=extract_keywords,
    inputs=text_input,
    outputs=output_text,
    title="Keyword Extraction model by Anurag S",
    description="Enter some text and get keywords extracted.",
    css = custom_css
).launch()