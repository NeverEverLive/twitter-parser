from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.requests import Request

from src.views.health import router as health_router
from src.views.tweets import router as tweet_router

def create_app():
    app = FastAPI(title="Twitter user parser", debug=False)

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    @app.exception_handler(Exception)
    async def unicorn_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=400,
            content={"success": False, "message": str(exc)},
        )


    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={"success": False, "message": str(exc)},
        )

    app.include_router(
        health_router,
        prefix="/api",
        tags=["Health"],
    )

    app.include_router(
        tweet_router,
        prefix="/api",
        tags=["Health"],
    )
    
    return app
