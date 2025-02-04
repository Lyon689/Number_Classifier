from main import app
import uvicorn

# This file is specifically for Vercel deployment
# Vercel looks for an app or a function to deploy

# Optional: If you want more explicit configuration
def create_app():
    return app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)