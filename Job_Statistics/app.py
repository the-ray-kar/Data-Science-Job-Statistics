import pickle as pkl
import plotly.express as px
import gradio as gr
from pydantic import BaseModel, Field
from typing import List

with open("job_stack_count.pkl", "rb") as f:
    job_stack_count = pkl.load(f)

job_stack_count['Generative_AI_Frameworks']['Pydantic'] = 1
job_stack_count['Programming_Languages']['C#'] = 1

class TechStack(BaseModel):
    GPU_Frameworks: List[str] = Field(..., alias="GPU Frameworks")
    Programming_Languages: List[str] = Field(..., alias="Programming Languages")
    Generative_AI_Frameworks: List[str] = Field(..., alias="Generative AI Frameworks")
    Databases: List[str] = Field(..., alias="Databases")
    Orchestration_Deployment: List[str] = Field(..., alias="Orchestration & Deployment")
    APIs_Web_Frameworks: List[str] = Field(..., alias="APIs & Web Frameworks")
    Big_Data_Technologies: List[str] = Field(..., alias="Big Data Technologies")
    Cloud_Platforms_Services: List[str] = Field(..., alias="Cloud Platforms & Services")
    Machine_Learning_Deep_Learning_Libraries: List[str] = Field(..., alias="Machine Learning & Deep Learning Libraries")
    Data_Visualization_Tools: List[str] = Field(..., alias="Data Visualization Tools")
    CI_CD_MLOps: List[str] = Field(..., alias="CI/CD & MLOps")
    Model_Formats_Optimization: List[str] = Field(..., alias="Model Formats & Optimization")
    Qualifications: List[str] = Field(..., alias="Qualifications")
    Machine_Learning_AI_Techniques: List[str] = Field(..., alias="Machine Learning & AI Techniques")
    Machine_Learning_AI_Models: List[str] = Field(..., alias="Machine Learning & AI Models")
    Tasks_Responsibilities: List[str] = Field(..., alias="Tasks & Responsibilities")
    Soft_Skills: List[str] = Field(..., alias="Soft Skills")
    Miscellaneous: List[str] = Field(..., alias="Miscellaneous")

    class Config:
        populate_by_name = True

# Load the job stack count data
with open("job_stack_count.pkl", "rb") as f:
    job_stack_count = pkl.load(f)

# Load the user's stack data
with open("all_my_stacks.pkl", "rb") as f:
    mynew_stacks = pkl.load(f)

def generate_treemap(category: str):
    """Generate a treemap visualization for the selected category."""
    if category not in job_stack_count:
        return "Category not found"
    
    stat_dict = job_stack_count[category]
    stat_dict_keys = list(stat_dict.keys())
    stat_dict_values = list(stat_dict.values())
    total = len(mynew_stacks)
    
    stat_dict_perc = [val / total * 100 for val in stat_dict_values]
    hover_text = [f"{label}: Covers {p:.0f}% of Job Descriptions" for label, p in zip(stat_dict_keys, stat_dict_perc)]
    
    fig = px.treemap(
        names=stat_dict_keys,
        parents=["" for _ in stat_dict_keys],
        values=stat_dict_values,
        hover_name=hover_text
    )
    fig.update_layout(title=category)
    return fig

# Create a Gradio interface in vertical layout
categories = list(job_stack_count.keys())
with gr.Blocks() as demo:
    gr.Markdown("# Data Science Tech Stack Treemap Visualization")
    gr.Markdown("Select a category to visualize the distribution of job tech stacks.")
    
    with gr.Column():  # Ensures vertical layout
        category_input = gr.Dropdown(choices=categories, label="Select Category")
        output_plot = gr.Plot()
    
    category_input.change(generate_treemap, inputs=category_input, outputs=output_plot)

demo.launch()

# Launch the app
demo.launch()
