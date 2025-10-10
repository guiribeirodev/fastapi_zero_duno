from http import HTTPStatus

from fastapi import FastAPI

from .schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}


@app.get('/hellohtml', status_code=HTTPStatus.OK)
def read_html():
    return """
    <html>
        <head>
            <title>Hello HTML</title>
        </head>
        <body>
            <h1>Hello, HTML!</h1>
        </body>
    </html>
    """
