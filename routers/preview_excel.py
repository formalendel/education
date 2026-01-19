import pandas as pd
from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="G:\\projects\\python\\papachka\\templates\\")
FILE_PATH = "G:\\projects\\python\\papachka\\Debet_pay.xlsx"
end_date = 'Дата погашения'

@router.get("/preview")
async def preview_excel(request: Request):
    dataframe = pd.read_excel(FILE_PATH)
    html_table = dataframe.to_html(classes="table table-striped", index=False)
    return templates.TemplateResponse("form_prev.html", {"request": request, "table_html": html_table})
