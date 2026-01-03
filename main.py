from fastapi import FastAPI

app = FastAPI(
    title="ScholarSight",
    description="AI-powered research paper summarization and similarity system",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}
