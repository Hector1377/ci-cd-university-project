from fastapi import FastAPI

app = FastAPI(
    title="CI/CD Python Project",
    description="University project demonstrating CI/CD with GitHub Actions",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to CI/CD Python Project"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
