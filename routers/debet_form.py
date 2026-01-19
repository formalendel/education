import pandas as pd
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from datetime import datetime
from fastapi.templating import Jinja2Templates
from fastapi import Request
from typing import Optional
from fastapi import Query

router = APIRouter()

templates = Jinja2Templates(directory="G:\\projects\\python\\papachka\\templates\\")
FILE_PATH = "G:\\projects\\python\\papachka\\Debet_pay.xlsx"
time_difference = 'Срок до погашения (дней)'
sort_by_default = 'name'


@router.get("/preview/debet", response_class=HTMLResponse)
async def preview_debet_pay(request: Request, sort_by: Optional[str] = Query("name", description="Ключ для сортировки")):
    dataframe=pd.read_excel(FILE_PATH)
    dataframe['долг'] = dataframe['Сумма договора'] - dataframe['Оплачено']
    filtered_df = dataframe[dataframe['долг'] > 0]
    today = pd.to_datetime(datetime.now())
    filtered_df[time_difference] = (filtered_df['Дата погашения'] - today).dt.days
    result = filtered_df[['Ф.И.О.', 'долг', time_difference]]
    html_table = (result).sort_values(by=[sort_by]).to_html(classes="table", index=False)
    #html_table = result.to_html(classes="table", index=False)
    return templates.TemplateResponse(request, "form_preview_debet.html", {'request': request, "items": html_table})
