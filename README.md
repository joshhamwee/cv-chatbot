
# Conversational Retrieval Chain API

This project is a FastAPI application that provides a Conversational Retrieval Chain model as a service. This model allows users to ask questions and get answers in a conversational manner, where the answers are retrieved from a given PDF document. The model has been trained to answer in the first person as "John Smith".

## Getting Started

These instructions will help you set up the project and understand how it works.

### Prerequisites

- Python 3.11
- Docker (optional)

### Setting Up

1. Clone the repository to your local machine.
2. Install the necessary Python dependencies. You can do this by running `pip install -r requirements.txt` in your project directory. If you're using Docker, this step is handled in the Dockerfile.

### Understanding the Code

The code consists of several key parts:

- `from langchain.* import *`: These imports bring in the necessary modules from the Langchain library, which provides the underlying functionality for conversational retrieval.
- `os.environ['OPENAI_API_KEY'] = ""`: This sets the OpenAI API key environment variable. You need to provide your own OpenAI API key here.
- `get_prompt(question)`: This function takes a question and formats it to ensure the model responds in the first person as "John Smith".
- `load_split_pdf(filepath)`: This function takes the path to a PDF document, loads it, and splits it into sections.
- `get_answer(question)`: This function takes a question and returns the model's answer.

### Running the Application

You can run the application using either Python directly or Docker. To use Python, execute `uvicorn main:app --reload` in your project directory. If you're using Docker, you can build the Docker image with `docker build -t my-fastapi-app .` and then run the application with `docker run -p 80:80 my-fastapi-app`.

## API Usage

The API exposes a single endpoint, `POST /ask`, which accepts a JSON body with a single field `content` representing the question. It returns a JSON response with a single field `answer`, which is the model's answer to the question.

For example:

```bash
curl -X POST "http://localhost:8000/ask" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{"content":"What is the meaning of life?"}"
```

Will return:

```json
{"answer":"The meaning of life is..."}
```

Please replace "What is the meaning of life?" with your actual question.
