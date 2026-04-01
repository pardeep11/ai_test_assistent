from fastapi import FastAPI

app = FastAPI()

def run_pipeline(error_text: str):
    return f"Analyzed Error: {error_text}"

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/analyze")
def analyze(error: str):
    result = run_pipeline(error)
    return {"analysis": result}