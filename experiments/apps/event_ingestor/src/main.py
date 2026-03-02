import logging
import os

import uvicorn

from src.app.asgi import create_app


app = create_app()


def main():
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    log_level = logging.getLevelName(os.getenv("LOG_LEVEL", "INFO").upper())
    uvicorn.run(app, host=host, port=port, log_level=log_level)


if __name__ == "__main__":
    main()
