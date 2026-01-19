from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import home
from routers import preview_excel
from routers import users_form
from routers import debet_form

app = FastAPI()
# Something2
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(home.router)
app.include_router(preview_excel.router)
app.include_router(users_form.router)
app.include_router(debet_form.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
