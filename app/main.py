import uvicorn
from fastapi import FastAPI, Depends

from app.database import get_session
from app.routers import AllRouters

app = FastAPI(dependencies=[Depends(get_session)])

app.include_router(AllRouters.router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)