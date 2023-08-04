from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import model as model

app = FastAPI()


class Question(BaseModel):
    content: str


@app.post("/ask")
async def ask_question(question: Question):
    # use the model to get the answer
    answer = model.get_answer(question.content)

    return {"answer": answer}


@app.get("/info")
async def getInfo():
    return {"info":  "Use this API to ask Josh any question"}

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=80)
