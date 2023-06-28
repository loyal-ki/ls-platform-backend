

from fastapi import FastAPI
from src.constants.constants import APP_NAME, VERSION, ROOT_PATH
from starlette.middleware.cors import CORSMiddleware
from src.routers import routers


def get_app():
    app = FastAPI(title=APP_NAME, version=VERSION,
                  docs_url="/", redoc_url="/redoc", root_path=ROOT_PATH)

    app.include_router(routers)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["Content-Disposition"],
    )

    @app.get("/", tags=["root"])
    def root():
        return {"server": APP_NAME}

    return app


# Run app
app = get_app()
