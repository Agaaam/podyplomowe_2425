import random
from fastapi import FastAPI, Response
import uvicorn
from datetime import datetime

app = FastAPI()

#Prosty endppoint zwracający tekst
@app.get("/")

def hello():
    return {"message":"witaj w moim API"}

@app.get("/weather/simple")
def get_weather_simple():
    return {
        "temperature": 36.6,
        "humidity": 70,
        "timestamp": datetime.now()
    }

@app.get("/weather/{station_id}")
def get_weather_by_station(station_id: str):
    return {
        "station_id": station_id,
        "temperature": random.uniform(15,25),
        "humidity": random.uniform(40, 80),
        "timestamp": datetime.now().timestamp()
    }


#----------------------------Przykład xml----------------------
#Uważać tutaj na spacje i dodatkowe entery
@app.get("/weather/")
def get_weather_query(city: str, format: str="json"):
    data = {
        "city": city,
        "temperature": random.uniform(15,25),
        "humidity": random.uniform(40, 80),
        "timestamp": datetime.now()
    }

    if format  == "xml":
        xml_data = f"""<?xml version="1.0"?>
        <weather>
            <city>{city}</city>
            <temperature>{data['temperature']}</temperature>
            <humidity>{data['humidity']}</humidity>
            <timestamp>{data['timestamp']}</timestamp>
        </weather>
        """
        return Response(content=xml_data, media_type="application/xml")

    return data
#Żeby to odczytać nalezy dodac miasto do www: http://127.0.0.1:8000/weather/?city=Torun

#------------Koniec XML ---------------
#---------------------------------------------------------------

#Przykład z HTML:
# @app.get("/html", response_class=HTMLResponse)
# def html():
#     return """
# <html>
# <head>
# <title>Witaj w moim API</title>
# </head>
# <body>
# <h1>Witaj w moim api</h1>
# </body>
# </html>"""
# #Wtedy widzimy inaczej na stronie: http://127.0.0.1:8000/html niż tutaj http://127.0.0.1:8000

# if __name__= "__main__":
uvicorn.run(app, host="127.0.0.1", port=8000)

