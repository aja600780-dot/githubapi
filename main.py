from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI(
    title="GitHub API",
    description="A RESTful API for GitHub operations",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to GitHub API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "users": "/api/users/{username}",
            "repos": "/api/repos/{owner}/{repo}"
        }
    }

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "ok"}

@app.get("/api/users/{username}")
def get_user(username: str):
    """Get user information"""
    return {
        "username": username,
        "message": f"User {username} endpoint - implement GitHub user lookup"
    }

@app.get("/api/repos/{owner}/{repo}")
def get_repo(owner: str, repo: str):
    """Get repository information"""
    return {
        "owner": owner,
        "repo": repo,
        "message": f"Repository {owner}/{repo} endpoint - implement GitHub repo lookup"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
