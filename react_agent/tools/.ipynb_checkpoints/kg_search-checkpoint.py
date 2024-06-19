import os
import yaml
from dotenv import load_dotenv
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS



example_prompt = PromptTemplate(
    input_variables = ["question", "cypher"],
    template = "Question: {question}\nCypher: {cypher}"
)

# Question-Cypher pair examples
with open("prompts/cypher_examples.yaml", "r") as f:
    example_pairs = yaml.safe_load(f)
    
examples = example_pair["examples"]

# LLM for choose the best similar examples
load_env()
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

embedding_model = GoogleGenerativeAIEmbeddings(
    model= "models/text-embedding-004"
)

example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples = examples,
    embeddings = embedding_model,
    vectorstore_cls = FAISS,
    k = 3
)

# Load schema, prefix, suffix
with open("prompts/schema.txt", "r") as file:
    schema = file.read()
    
with open("prompts/cypher_instruct.yaml", "r") as file:
    instruct = yaml.safe_load(file)
    
dynamic_prompt = FewShotPromptTemplate(
    example_selector = example_selector,
    example_prompt = instruct["example_template"],
    prefix = instruct["prefix"],
    suffix = instruct["suffix"].format(schema),
    input_variables = ["question"]
)
    
if __name__ == "__main__":
    print(dynamic_prompt.format(question = "What does the Software Engineer job usually require?"))