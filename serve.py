from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment.")

model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer the user's questions."),
    ("user", "{text}")
])
parser = StrOutputParser()
chain = prompt | model | parser

app = FastAPI(title="Langchain Server", version="1.0")

class ChainRequest(BaseModel):
    text: str
    language: str

@app.post("/chain")
async def run_chain(request: ChainRequest):
    response = await chain.ainvoke({
        "text": request.text,
    })
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
