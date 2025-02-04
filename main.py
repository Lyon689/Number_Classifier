from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import math
import requests

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

def is_armstrong_number(n):
    """
    Check if a number is an Armstrong number.
    An Armstrong number is a number that is the sum of its own digits 
    each raised to the power of the number of digits.
    """
    # Convert number to string to easily iterate through digits
    str_n = str(n)
    num_digits = len(str_n)
    
    # Calculate sum of each digit raised to the power of number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in str_n)
    
    return armstrong_sum == n

def get_number_fact(number):
    """
    Retrieve a fun fact about the number from Numbers API
    """
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math")
        return response.text if response.status_code == 200 else "No interesting fact found"
    except Exception:
        return "Unable to retrieve fact"

@app.get("/api/classify-number")
async def classify_number(number: str = Query(..., description="Number to classify")):
    try:
        # Validate input is a number
        n = int(number)
    except ValueError:
        raise HTTPException(status_code=400, detail={
            "number": number,
            "error": True
        })

    # Determine properties
    properties = []
    if is_armstrong_number(n):
        properties.append("armstrong")
    
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    # Get fun fact
    fun_fact = get_number_fact(n)

    return {
        "number": n,
        "is_prime": all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)) if n > 1 else False,
        "is_perfect": sum(i for i in range(1, n) if n % i == 0) == n if n > 0 else False,
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(n)),
        "fun_fact": fun_fact
    }



# For local development server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)