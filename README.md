<h1 align="center"><b>MultiHop Question Answering with KnowledgeGraph</b></h1>

<h3 align="center"><b>HCMUS - NLP Group Project - Semester II/2023-2024</b></h3>


## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
    - [Clone the github repo](#clone-the-github-repo)
    - [Install requirements](#install-requirements)
    - [Scrape job posts from Indeed](#scrape-job-posts-from-indeed)
    - [Construct & Update Knowledge Graph](#construct--update-knowledge-graph)
    - [QA with LLM](#qa-with-llm)
- [Components](#components)
    - [Data Collection Module](#data-collection-module)
    - [Knowledge Graph Module](#knowledge-graph-module)
    - [Inference Module](#inference-module)
- [Key Features](#key-features)
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
### Data Collection Module
This module is responsible for automaticaly scraping and collecting job post data on a daily basis.

![Data Collection Module](images/data_collection_module.png?raw=True)
### Knowledge Graph Module
This module acts as an information processor. It extracts entities and relationships from incoming data, and then uses this information to update the knowledge graph itself.

![Knowledge Graph Module](images/knowledge_graph_module.png?raw=True)
### Inference Module
This module is responsible for generating responses to user's queries. A ReAct agent with 2 tools (Knowledge Graph Search and Tavily Search) is the core of this module.

![Inference Module](images/inference_module.png?raw=True)
## Key Features

## References

## Tech Stack
<img src="https://github-readme-tech-stack.vercel.app/api/cards?align=center&lineCount=2&line1=githubactions%2Cgithub+actions%2C316f90%3Bselenium%2Cselenium%2C478d47%3Bdata%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB2ZXJzaW9uPSIxLjEiIHZpZXdCb3g9IjAgMCAxNjAwIDE2MDAiIHdpZHRoPSIxMjgwIiBoZWlnaHQ9IjEyODAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI%2BCjxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDApIiBkPSJtMCAwaDE2MDB2MTYwMGgtMTYwMHoiIGZpbGw9IiNGRDAyNjMiLz4KPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNzkwLDI3MCkiIGQ9Im0wIDBoMjJsMTcgMiAyMiA2IDEzIDUgMTYgOCAxMyA4IDE2IDEzIDEzIDEzIDggMTAgMTAgMTUgMTAgMTkgNyAyMiA0IDIwIDEgOXYyN2wtNCAyMy02IDIwLTcgMTYtMTAgMTctOSAxMi05IDEwLTEwIDEwLTEwIDgtMTkgMTItMTQgNy0yMCA3LTI0IDYtNDggMTEtMjUgNi0zNSAxMi0xOSA4LTE5IDEwLTE3IDEwLTE3IDEyLTEwIDgtMTIgMTEtNSA1LTMtMS03LTEyLTEyLTE2LTEyLTEzLTE0LTExLTEwLTctMTEtNiAxLTQgMTItMTIgMTEtMTQgOC0xMSA4LTEzIDEyLTIxIDEwLTIyIDgtMjEgOC0yNyAxMC00MiA4LTM2IDctMjMgNy0xNiAxMi0yMCAxMS0xNCA5LTEwIDEwLTkgMTUtMTEgMTYtOSAxMy02IDE1LTUgMTgtNHoiIGZpbGw9IiNGRUZFRkQiLz4KPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOTg2LDkxMikiIGQ9Im0wIDAgNCAxIDEyIDE5IDEyIDE0IDcgOCAxNCAxMSAxMCA3IDEwIDUtMSA0LTcgNy0xMSAxNC0xMSAxNS0xMCAxNS0xMiAyMi04IDE3LTExIDMwLTYgMjAtOSAzNy04IDM3LTcgMjQtNiAxNS04IDE2LTkgMTMtMTEgMTQtMTMgMTMtMTcgMTMtMTggMTAtMTkgOC0xOSA1LTE5IDNoLTMxbC0yMi00LTE1LTQtMTktOC0xMy03LTEzLTktMTUtMTMtOC04LTExLTE0LTEwLTE2LTktMTktNy0yMS00LTIydi0zMmwzLTE5IDQtMTYgOC0yMCAxMC0xOCAxMi0xNiA3LTcgNy04IDE0LTEyIDI1LTE1IDIyLTkgMjItNiAyNy02IDM5LTkgMjEtNiAzMC0xMCAyNi0xMiAxNS04IDEzLTggMTAtNyAxMi05IDEzLTExIDUtNXoiIGZpbGw9IiNGRUZFRkQiLz4KPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNDEyLDYzOCkiIGQ9Im0wIDBoMzdsMTkgMyAxNSA0IDE1IDYgMTYgOCAxMSA3IDE0IDExIDE3IDE3IDggMTAgMTIgMTkgNyAxNSAxMCAzMiAxMiA1NCA3IDI3IDYgMTkgOSAyNSAxNiAzMyA3IDExIDEwIDE1IDExIDE0IDEyIDE0IDUgNS0yIDQtOCA0LTEzIDktMTUgMTMtMTAgMTEtMTIgMTctNiAxMS00LTItMTAtMTAtMTAtOC0xNS0xMS0xNy0xMS0yNi0xNC0yMS05LTM2LTEyLTQ1LTExLTI4LTYtMjYtNy0xNi02LTE2LTgtMTgtMTItMTQtMTItOS05LTEzLTE3LTktMTUtOS0yMC02LTIxLTQtMjR2LTIybDMtMjAgNC0xNyA3LTE5IDctMTQgMTAtMTUgOS0xMSA1LTYgNS01IDEzLTExIDE1LTEwIDE0LTggMTItNSAxNS01eiIgZmlsbD0iI0ZFRkVGRCIvPgo8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSg5NzgsNTQ0KSIgZD0ibTAgMCA0IDIgOSA5IDEwIDggMTggMTMgMTQgOSAyMiAxMiAxOSA5IDI0IDkgMjUgNyAxOSA1IDM0IDcgMjggNyAxNiA1IDEzIDUgMTkgMTAgMTAgNyAxMCA4IDEyIDExIDEyIDEzIDEwIDE1IDYgMTAgOCAyMCA1IDE2IDMgMTUgMiAxOS0xIDIxLTMgMTktNiAyMC03IDE3LTcgMTMtMTAgMTQtOSAxMS0xMiAxMi0xOSAxNC0xOCAxMC0xNCA2LTE2IDUtMTkgNC0xMiAxaC0yNGwtMTgtMy0xOS01LTEzLTUtMTYtOC0xNy0xMS0xMy0xMS0xMS0xMS0xMS0xNC0xMi0yMC05LTIxLTgtMjctNC0xOC0xMS00OC00LTE0LTctMjMtMTAtMjUtOC0xNy0xMS0xOS0xMC0xNS0xMC0xMy0xMi0xNC03LTd2LTNsMTQtOCAxNC0xMSAxMC05IDktMTAgOS0xMiA3LTExeiIgZmlsbD0iI0ZFRkVGRCIvPgo8L3N2Zz4K%2Cchainlit%2C%3B&line2=langchain%2Clangchain%2C3b7452%3Bpython%2Cpython%2C0f74a1%3Bdata%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB2ZXJzaW9uPSIxLjEiIHZpZXdCb3g9IjAgMCA4MDAgODAwIiB3aWR0aD0iMTI4MCIgaGVpZ2h0PSIxMjgwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwKSIgZD0ibTAgMGg4MDB2ODAwaC04MDB6IiBmaWxsPSIjRkVGREZEIi8%2BCjxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDI4MywxMDIpIiBkPSJtMCAwaDExbDkgMyA4IDggMTAgMTQgMTYgMjEgMTAgMTQgMTYgMjEgMTQgMTkgMTIgMTYgNSAxMCAxIDR2OWwtNSAxMC03IDctNSAzLTUgMWgtMTBsLTEwLTQtOS05LTE0LTE5LTExLTE1LTMtNC0xIDc3djIwNmwtNS00LTEyLTYtMTAtMi0xMiAzLTE0IDctMS03LTEtMjc0LTkgMTItMTQgMTktOSAxMS04IDctNyAyaC0xMGwtOS0zLTktOS0zLTl2LTEybDQtOSAyOC0zOCAxNi0yMSAxMi0xNiAxMy0xOCAxMi0xNiA3LTZ6IiBmaWxsPSIjRjE1NTI5Ii8%2BCjxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDUzOSw0MTgpIiBkPSJtMCAwIDEwIDEgMTIgNiAxOCAxMyAxMyAxMCAyMSAxNiAzOCAyOCAxMyAxMCA2IDUgNSA4IDIgOC0xIDEwLTQgOC0xMiAxMS0xOSAxNC0xMSA4LTE5IDE0LTEzIDEwLTM2IDI3LTExIDYtMTAgMS0xMC0zLTctNS02LTktMS0zdi0xNmw1LTggNS01IDEwLTggMTgtMTMgMTItOHYtMWwtOTgtMWgtMTQybC0yMy0xdi00bDEwLTggNi05IDEtNXYtMTRsLTQtMTNoMjUxdi0ybC01LTItMTktMTQtMTMtMTAtMTAtMTAtNC04LTEtNHYtOWw0LTkgOS04eiIgZmlsbD0iI0ZFQjcwOCIvPgo8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyODgsNDgxKSIgZD0ibTAgMCAxMCAyIDE0IDcgNiA5IDQgMTJ2MTRsLTIgNi02IDktMTEgOS04IDItMTEgMS02IDUtOSAxMS0xMyAxNS0xMSAxMi04IDEwLTExIDEyLTkgMTAtMiA1IDI1LTYgMTMtM2gxNGw4IDUgNSA2IDMgMTAtMyAxMC01IDYtMTAgNS0zMCA3LTc4IDE3LTktMS04LTUtNi04LTItNXYtOWw2LTY3IDMtNDEgNC04IDctNiA0LTJoMTFsOCA0IDYgNyAzIDd2MTBsLTMgMzB2N2w2LTUgOC0xMCA5LTEwIDktMTEgMTEtMTIgOS0xMSAxMi0xNCA4LTkgMS0xMiA0LTkgNS04IDE1LTh6IiBmaWxsPSIjMDVBMEVFIi8%2BCjxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDI4OCw0ODEpIiBkPSJtMCAwIDEwIDIgMTQgNyA2IDkgNCAxMnYxNGwtMiA2LTYgOS0xMSA5LTggMi0xMSAxLTQgMnYtNGwtNy0yLTEwLTgtNy04LTItNXYtMTlsNC05IDUtOCAxNS04eiIgZmlsbD0iIzMzQUU4NCIvPgo8L3N2Zz4K%2Ctavily%2C%3Bneo4j%2Cneo4j%2C337da4%3B" alt="My Tech Stack" />

## **Contributors**
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
