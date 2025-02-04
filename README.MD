# Number Classification API

## Overview
This FastAPI-based microservice classifies numbers and provides interesting mathematical properties.

## Features
- Determines if a number is:
  - Armstrong number
  - Prime
  - Perfect number
  - Even or Odd
- Calculates digit sum
- Retrieves a fun mathematical fact about the number

## Setup & Installation

### Prerequisites
- Python 3.8+
- pip

### Install Dependencies

pip install -r requirements.txt

### Run Locally

uvicorn main:app --reload

## API Endpoint
`GET /api/classify-number?number=371`

### Response Example
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number..."
}
```

## Error Handling
Invalid inputs return a 400 Bad Request with error details.

## Technologies
- FastAPI
- Python
- Numbers API (for fun facts)