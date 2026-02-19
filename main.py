from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "🎓 CI/CD Python Project ✅", "repo": "Hector1377"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
