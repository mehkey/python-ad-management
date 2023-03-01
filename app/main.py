import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.database import get_session
from app.routers import AllRouters

app = FastAPI(dependencies=[Depends(get_session)])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(AllRouters.router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)