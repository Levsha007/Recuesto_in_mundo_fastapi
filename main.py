from fastapi import FastAPI, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database.database import engine, Base, SessionLocal
from models.models import Item, HotelBooking, DiveBooking, DiveSubscription
from pydantic import BaseModel, ValidationError
from dotenv import load_dotenv
from datetime import datetime

# Загрузка переменных окружения из файла .env
load_dotenv()

# Создание экземпляра FastAPI
app = FastAPI()

# Настройка шаблонизатора Jinja2 для рендеринга HTML-шаблонов
templates = Jinja2Templates(directory="templates")

# Настройка статических файлов (CSS, JavaScript, изображения)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Создание таблиц в базе данных на основе моделей, определенных в models.models
Base.metadata.create_all(bind=engine)

# Модель данных для создания нового товара
class ItemCreate(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db  # Возвращает сессию базы данных
    finally:
        db.close()  # Закрывает сессию после использования

# Маршрут для отображения главной страницы
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Маршрут для отображения страницы с информацией об океанариумах
@app.get("/aquariums", response_class=HTMLResponse)
async def read_aquariums(request: Request):
    return templates.TemplateResponse("aquariums.html", {"request": request})

# Маршрут для отображения страницы с информацией о дайвинге
@app.get("/dayving", response_class=HTMLResponse)
async def read_dayving(request: Request):
    return templates.TemplateResponse("dayving.html", {"request": request})

# Маршрут для отображения формы бронирования дайвинга
@app.get("/form_dvg", response_class=HTMLResponse)
async def read_form_dvg(request: Request):
    return templates.TemplateResponse("form_dvg.html", {"request": request})

# Маршрут для отображения формы оформления абонемента на дайвинг
@app.get("/form_dvg_abt", response_class=HTMLResponse)
async def read_form_dvg_abt(request: Request):
    return templates.TemplateResponse("form_dvg_abt.html", {"request": request})

# Маршрут для отображения формы бронирования отеля
@app.get("/form_hotel_brn", response_class=HTMLResponse)
async def read_form_hotel_brn(request: Request):
    return templates.TemplateResponse("form_hotel_brn.html", {"request": request})

# Маршрут для отображения страницы с результатами
@app.get("/resultPage", response_class=HTMLResponse)
async def read_resultPage(request: Request):
    return templates.TemplateResponse("resultPage.html", {"request": request})

# Маршрут для получения информации о товаре по его ID
@app.get("/api/items/{item_id}")
async def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Маршрут для создания нового товара
@app.post("/api/items/")
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Маршрут для отображения всех бронирований отелей
@app.get("/get_hotel_bookings", response_class=HTMLResponse)
async def get_hotel_bookings(request: Request, db: Session = Depends(get_db)):
    bookings = db.query(HotelBooking).all()
    return templates.TemplateResponse("hotel_bookings.html", {"request": request, "bookings": bookings})

# Маршрут для отображения всех бронирований дайвинга
@app.get("/get_dive_bookings", response_class=HTMLResponse)
async def get_dive_bookings(request: Request, db: Session = Depends(get_db)):
    bookings = db.query(DiveBooking).all()
    return templates.TemplateResponse("dive_bookings.html", {"request": request, "bookings": bookings})

# Маршрут для отображения всех подписок на дайвинг
@app.get("/get_dive_subscriptions", response_class=HTMLResponse)
async def get_dive_subscriptions(request: Request, db: Session = Depends(get_db)):
    subscriptions = db.query(DiveSubscription).all()
    return templates.TemplateResponse("dive_subscriptions.html", {"request": request, "subscriptions": subscriptions})

# Маршрут для обработки данных из формы оформления абонемента на дайвинг
@app.post("/submit_dive_subscription")
async def submit_dive_subscription(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    duration: str = Form(...),
    start: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        start_date = datetime.strptime(start, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format")

    subscription = DiveSubscription(
        name=name,
        email=email,
        phone=phone,
        duration=duration,
        start=start_date
    )
    db.add(subscription)
    db.commit()
    db.refresh(subscription)
    return JSONResponse(content={"success": True, "message": "Заказ успешно оформлен!"})

# Маршрут для обработки данных из формы бронирования отеля
@app.post("/submit_hotel_booking")
async def submit_hotel_booking(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    checkin: str = Form(...),
    checkout: str = Form(...),
    room: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        checkin_date = datetime.strptime(checkin, "%Y-%m-%d").date()
        checkout_date = datetime.strptime(checkout, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format")

    booking = HotelBooking(
        name=name,
        email=email,
        phone=phone,
        checkin=checkin_date,
        checkout=checkout_date,
        room=room
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return JSONResponse(content={"success": True, "message": "Заказ успешно оформлен!"})

# Маршрут для обработки данных из формы бронирования дайвинга
@app.post("/submit_dive_booking")
async def submit_dive_booking(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    date: str = Form(...),
    location: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        date_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format")

    booking = DiveBooking(
        name=name,
        email=email,
        phone=phone,
        date=date_date,
        location=location
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return JSONResponse(content={"success": True, "message": "Заказ успешно оформлен!"})