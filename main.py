import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.users import users
from app.contents import contents

app = FastAPI()

app.mount("/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/htmls")

app.include_router(users.router)
app.include_router(contents.router)

@app.get("/")
async def read_root(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("main.html", context)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
