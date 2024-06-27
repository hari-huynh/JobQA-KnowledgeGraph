import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import BaseTool, StructuredTool, tool





load_dotenv()

os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")



@tool
def tavily_search( question: str) -> str:

    """
    useful for when you need to answer questions about
    informations such as: jobs, companies, etc which knowledge graph have not.
    """


    tool_search = TavilySearchResults()
    tool_search.description="""You are an expert at finding information about the job,
        the company, and the skills required for that job.
        Try to find out what is relevant to the company, the job, and the skills required for that job.
        If the questions are not relevant, answer them in your own words."""



    prompt_search=f"""You are an expert at finding information about the job,
        the company, and the skills required for that job.
        Try to find out what is relevant to the company, the job, and the skills required for that job.
        If the questions are not relevant, answer them in your own words.

        Query: {question}"""

    result=tool_search.invoke({"query":prompt_search})

    llm_chat = ChatGoogleGenerativeAI(
        model= "gemini-1.5-flash-latest"
    )
    content=[]
    for i in result:
        content.append(i['content'])

    prompt=f"""

    You are a career consultant, based on the information you have  contents: {content},
    consider yourself an expert to summarize summary details not too short the content and
    highlight the content related to the company's job and the necessary skills and return must 1 URL

    You can add information you know about the question {question}
    """
    response=llm_chat.invoke(prompt)
    response= response.content.replace("\n"," ")
  
  
    thought = "Tavily Search. Search for information when Knowledge Graph has no information"
    action = f"Summarize details: {response}"
  
    return f"Thought: {thought}\nAction: {action}"


if __name__ == "__main__":
    question = "I want to know about AI Engineering at Viettel?"
    
    result=tavily_search(question)
    
    print(result)
    
    
