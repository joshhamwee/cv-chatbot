from fastapi import FastAPI
from pydantic import BaseModel

import model

app = FastAPI()


class Question(BaseModel):
    content: str


@app.post("/ask")
async def ask_question(question: Question):
    # Here is where you'd put your pre-made function to process the question
    # For now, it just returns the question back as the answer

    answer = model.get_answer(question.content)

    return {"answer": answer}
