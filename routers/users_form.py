from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import pandas as pd

router = APIRouter()

FILE_PATH = "G:\\projects\\python\\papachka\\Debet_pay.xlsx"
templates = Jinja2Templates(directory="G:\\projects\\python\\papachka\\templates\\")
end_date = 'Дата погашения'
# form_route = APIRouter("/form")

def get_excel_columns(failname=FILE_PATH):
    dataframe = pd.read_excel(failname)
    return dataframe.columns.tolist()


@router.get("/form", response_class=HTMLResponse)
async def read_root(request: Request):
    columns = get_excel_columns()
    return templates.TemplateResponse("form.html", {"request": request, "columns": columns})


@router.post("/form/submit")
async def submit_form(request: Request):
    form_data = await request.form()
    row = pd.DataFrame([form_data])
    row[end_date] = pd.to_datetime(row[end_date], format='%Y-%m-%d')
    dataframe = pd.read_excel(FILE_PATH)
    dataframe = pd.concat([dataframe, row], ignore_index=True)
    dataframe.to_excel(FILE_PATH, sheet_name='Sheet1', index=False)
    return RedirectResponse(url="/preview", status_code=303)
