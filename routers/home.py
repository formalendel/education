from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="G:\\projects\\python\\papachka\\templates\\")
FILE_PATH = "G:\\projects\\python\\papachka\\Debet_pay.xlsx"


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
