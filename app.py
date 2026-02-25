from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import ollama
import os 

app=FastAPI()

#templates  
templates =Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"),name="static")


#request models
@app.get("/",response_class=HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/generate")
async def generate(data:dict):
    word=data["word"]
    prompt = f"""
    For the English word "{word}" give:

    1. Simple meaning
    2. One example sentence
    3. 3 synonyms
    4. One multiple-choice quiz question

    Keep answers short and clear.
    """
    response=ollama.chat(
        model="llama3.2:3b",
        messages=[{"role":"user","content":prompt}]
    )
    return {"result":response["message"]["content"]}


