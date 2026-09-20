from fastapi import FastAPI
from pydantic import BaseModel 

from backend.statistics.statics import (
    mean,
    median,
    mode,
    minimum,
    maximum,
    data_range,
    first_quartile,
    third_quartile,
    interquartile_range,
    variance,
    standard_deviation,
    outliers,
)

app = FastAPI()

class DataRequest(BaseModel):
    data: list[float]


@app.get('/hello')
def hello():
    return {'Message': 'test'}

@app.post('/statistics')
def calculate_statics(request:DataRequest):
    data = request.data

    return {
        "mean": mean(data),
        "median": median(data),
        "mode": mode(data),
        "minimum": minimum(data),
        "maximum": maximum(data),
        "range": data_range(data),
        "q1": first_quartile(data),
        "q3": third_quartile(data),
        "iqr": interquartile_range(data),
        "variance": variance(data),
        "standard_deviation": standard_deviation(data),
        "outliers": outliers(data),
        "sorted_data": sorted(data),
    }

