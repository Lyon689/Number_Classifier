from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import math
import requests


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def is_armstrong_number(n):
    n = abs(n)
    str_n = str(n)
    num_digits = len(str_n)
    armstrong_sum = sum(int(digit) ** num_digits for digit in str_n)
    return armstrong_sum == n


def get_number_fact(number):
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math")
        return response.text if response.status_code == 200 else "No interesting fact found"
    except Exception:
        return "Unable to retrieve fact"


@app.get("/api/classify-number")
async def classify_number(number: str = Query(None)):
    if number is None:
        return {
            "number": "alphabet",
            "error": True
        }
    
    try:
        n = int(number)
    except ValueError:
        return {
            "number": number,
            "error": True
        }

    properties = []
    if is_armstrong_number(n):
        properties.append("armstrong")
    
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    digit_sum = sum(int(digit) for digit in str(abs(n)))
    fun_fact = get_number_fact(n)

    return {
        "number": n,
        "is_prime": False if n <= 1 else all(n % i != 0 for i in range(2, int(math.sqrt(abs(n))) + 1)),
        "is_perfect": False if n <= 0 else sum(i for i in range(1, n) if n % i == 0) == n,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}