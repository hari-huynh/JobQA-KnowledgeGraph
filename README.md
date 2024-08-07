<h1 align="center"><b>MultiHop Question Answering with KnowledgeGraph</b></h1>

<h3 align="center"><b>HCMUS - NLP Group Project - Semester II/2023-2024</b></h3>


## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
    - Clone the github repo
    - Install requirements
- [Components](#components)
- [Key Features](#key-features)
- [How to Use](#how-to-use)
- [References](#references)
- [Tech Stack](#tech-stack)

## Introduction
This project aims to develop a question answering system that can provide comprehensive and informative responses to queries related job postings. The core component of this system is a knowledge graph meticulously constructed from a vast amount of job postings. This knowledge graph serves as a robust Retrieval Augmented Generation (RAG) engine, enabling an advanced language model to effectively extract and process relevant information.


## Usage
### Clone the github repo
```bash
git clone https://github.com/hari-huynh/MultiHop-QA-KnowledgeGraph.git
```

### Install requirements
```bash
pip install requirements.txt
```
### Scrape job posts from Indeed
The knowledge graph is constructed from job posts scraped from Indeed. To scrape job post information from Indeed, use the following code:
```bash
cd knowledge_graph
python scrape_jd.py --url "indeed-url-for-scraping" --job "role-that-you-want-to-scrape" --loc "the-location"
```

Example:
```bash
python scrape_jd.py --url "https://vn.indeed.com/jobs" --job "Artificial Intelligence" --loc "Thành phố Hồ Chí Minh"
```
The result will be a JSON file containing several job posts and the corresponding information, such as titles, company names and job descriptions. See examples in the ```job_posts_data``` inside ```knowledge_graph``` folder.

### Construct & Update Knowledge Graph
```bash
python update_kg.py
```
This will create a knowledge graph with a predefined schema (If the knowledge graph hasn't been created yet) or update the knowledge graph with new data.


### QA with LLM
After having a knowledge graph filled with job post information, you can now start asking about job post related questions.
```bash
cd react_agent
python main.py
```

## Components
### Data Collection
![Data Collection Module](images/data_collection_module.png?raw=True)
### Knowledge Graph Maintenance
![Knowledge Graph Module](images/knowledge_graph_module.png?raw=True)
### Inference
![Inference Module](images/inference_module.png?raw=True)
## Key Features

## How to Use

## References

## Tech Stack


### **Contributors**
<table>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/hari-huynh>
            <img src=https://avatars.githubusercontent.com/u/142809008?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Casper/>
            <br />
            <sub style="font-size:14px"><b>hari-huynh</b></sub>
        </a>
    </td>
      <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/QuangTruong-Nguyen>
            <img src=https://avatars.githubusercontent.com/u/139192880?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Bailey Harrington/>
            <br />
            <sub style="font-size:14px"><b>QuangTruong-Nguyen</b></sub>
        </a>
    </td>
      <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/TaiQuach123>
            <img src=https://avatars.githubusercontent.com/u/92372685?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Yixin Shen/>
            <br />
            <sub style="font-size:14px"><b>TaiQuach123</b></sub>
        </a>
    </td>
</tr>
</table>
