from fastapi import FastAPI

from src.interfaces.api.routes.convert import router as convert_router
from src.interfaces.api.routes.download import router as download_router
from src.interfaces.api.routes.upload import router as upload_router

app = FastAPI(title="SVG to PNG Conversor")

# Include routers
app.include_router(upload_router, prefix="/api")
app.include_router(convert_router, prefix="/api")
app.include_router(download_router, prefix="/api")
