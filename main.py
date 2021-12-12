import uvicorn
from fastapi import FastAPI
from app.users import users
from app.contents import contents

app = FastAPI()


app.include_router(users.router)
app.include_router(contents.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
