from database import BaseDBModel, engine
from users.router import router
from fastapi import FastAPI
import uvicorn

BaseDBModel.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

@app.get("/")
async def root():
    return {"message": "всё работает"}
