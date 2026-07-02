from fastapi import FastAPI
from app.api.routes import router
from app.core.loggings import setup_logging

setup_logging()

app = FastAPI(title="GenAI ETL RAG System (Optimized)")

app.include_router(router)
