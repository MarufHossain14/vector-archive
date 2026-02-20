"""FastAPI app: image archive with semantic search (text -> image)."""

import uvicorn
from fastapi import FastAPI

from . import settings

app = FastAPI(
    title="vector-archive",
    description="Image archive: upload images, search by text.",
)


@app.get("/")
def root():
    return {"service": "vector-archive", "status": "ok"}


def main():
    uvicorn.run(
        "backend.app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
