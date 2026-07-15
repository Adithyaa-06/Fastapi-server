from fastapi import FastAPI

"""APP instance"""
app = FastAPI()
@app.get("/")
def root():
    return {
        "message": "Hello from my first FastAPI server!"
    }
#ABOUT 
@app.get("/about")
def about():
    return {
        "name": "Pranava Adithyaa Chapala",
        "role": "B.Tech Information Technology Student",
        "learning": "FastAPI"
    }