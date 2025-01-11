from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse

app = FastAPI()

#Prosty endppoint zwracający tekst
@app.get("/")

def hello():
    return {"message":"witaj w moim API"}

@app.get("/html", response_class=HTMLResponse)
def html():
    return """
<html>
<head>
<title>Witaj w moim API</title>
</head>
<body>
<h1>Witaj w moim api</h1>
</body>
</html>"""
#Wtedy widzimy inaczej na stronie: http://127.0.0.1:8000/html niż tutaj http://127.0.0.1:8000

# if __name__= "__main__":
uvicorn.run(app, host="127.0.0.1", port=8000)

