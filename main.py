from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import api.model as model

app = FastAPI()


class Question(BaseModel):
    content: str


@app.post("/ask")
async def ask_question(question: Question):
    # Here is where you'd put your pre-made function to process the question
    # For now, it just returns the question back as the answer

    answer = model.get_answer(question.content)

    return {"answer": answer}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=80)
