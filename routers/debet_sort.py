from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from typing import Optional
from fastapi.templating import Jinja2Templates
from fastapi import Request, Query

from debet_pay import pars_calculate_debet_payments

router = APIRouter()

templates = Jinja2Templates(directory="G:\\projects\\python\\papachka\\templates\\")
FILE_PATH = "G:\\projects\\python\\papachka\\Debet_pay.xlsx"
time_difference = 'Срок до погашения (дней)'

@router.get("/preview/debet/sort", response_class=HTMLResponse)
async def debet_pay_sort(request: Request, sort_by: Optional[str] = Query("name", description="Ключ для сортировки")):
    html_table = pars_calculate_debet_payments(FILE_PATH).sort_values(by=[sort_by]).to_html(classes="table", index=False)
    return templates.TemplateResponse(request, "form_debet_sort.html", {'request': request, "items": html_table})
