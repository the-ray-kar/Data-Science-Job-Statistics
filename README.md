# Job Statistics Visualization

This project visualizes the distribution of **167 job descriptions** collected from the internet. The descriptions cover various tech domains and frameworks, providing insights into the most common skills and technologies required across the industry.

### **Categories Analyzed**

The data is divided into the following key categories:

- **GPU Frameworks**
- **Programming Languages**
- **Generative AI Frameworks**
- **Databases**
- **Orchestration & Deployment**
- **APIs & Web Frameworks**
- **Big Data Technologies**
- **Cloud Platforms & Services**
- **Machine Learning & Deep Learning Libraries**
- **Data Visualization Tools**
- **CI/CD & MLOps**
- **Model Formats & Optimization**
- **Qualifications**
- **Machine Learning & AI Techniques**
- **Machine Learning & AI Models**
- **Tasks & Responsibilities**
- **Soft Skills**
- **Miscellaneous**

### **What It Does**

The project includes an interactive **treemap visualization** powered by **Gradio** and **Plotly**. Users can select different categories to explore how technologies and skills are distributed across job descriptions.

### **How to Use**

1. Select a **category** from the dropdown list.
2. The treemap will be generated, showing the distribution of job technologies within the selected category.
3. Hover over any section in the treemap to see the percentage of job descriptions that mention that specific technology.

### **Interactive Demo**

You can explore the interactive treemap visualization hosted on **Hugging Face** here:  
[**Job Statistics Visualization Demo**](https://huggingface.co/spaces/SparkleDark/Job_Statistics)

### **Technologies Used**

- **Gradio**: For creating the interactive web interface.
- **Plotly**: For visualizing the data with an interactive treemap.
- **Pydantic**: For structuring the data model.
- **Python**: For backend logic and data processing.
- **Pickle**: For serializing and deserializing data files.
