from fastapi import FastAPI
import os, openai

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def root():
    return {"message": "OpenHands backend is running"}

@app.post("/chat")
def chat(prompt: str):
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )
    return {"response": resp.choices[0].message["content"]}
