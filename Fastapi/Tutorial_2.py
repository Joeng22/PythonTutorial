import uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
   return {"message": "Hello World"}


if __name__=="__main__":
    uvicorn.run("main:Tutorial_2", host="127.0.0.1", port=8000,reload=True)

