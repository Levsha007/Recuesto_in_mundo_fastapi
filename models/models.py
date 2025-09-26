from sqlalchemy import Column, Integer, String, Date, Enum, Float
from database.database import Base

# Модель для хранения информации о товарах
class Item(Base):
    __tablename__ = "items"  # Имя таблицы в базе данных
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор товара
    name = Column(String, index=True)  # Название товара
    description = Column(String, index=True)  # Описание товара
    price = Column(Float, index=True)  # Цена товара
    tax = Column(Float, index=True)  # Налог на товар

# Модель для хранения информации о бронированиях отелей
class HotelBooking(Base):
    __tablename__ = "hotel_bookings"  # Имя таблицы в базе данных
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор бронирования
    name = Column(String, index=True)  # Имя клиента
    email = Column(String, index=True)  # Email клиента
    phone = Column(String, index=True)  # Телефон клиента
    checkin = Column(Date, index=True)  # Дата заезда
    checkout = Column(Date, index=True)  # Дата выезда
    room = Column(Enum("стандарт", "люкс", "семейный", name="room_type"), index=True)  # Тип номера

# Модель для хранения информации о бронированиях дайвинга
class DiveBooking(Base):
    __tablename__ = "dive_bookings"  # Имя таблицы в базе данных
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор бронирования
    name = Column(String, index=True)  # Имя клиента
    email = Column(String, index=True)  # Email клиента
    phone = Column(String, index=True)  # Телефон клиента
    date = Column(Date, index=True)  # Дата дайвинга
    location = Column(Enum("Blue Hole", "Great Barrier Reef", "Tubbataha Reef", name="dive_location"), index=True)  # Локация дайвинга

# Модель для хранения информации о подписках на дайвинг
class DiveSubscription(Base):
    __tablename__ = "dive_subscriptions"  # Имя таблицы в базе данных
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор подписки
    name = Column(String, index=True)  # Имя клиента
    email = Column(String, index=True)  # Email клиента
    phone = Column(String, index=True)  # Телефон клиента
    duration = Column(Enum("1 месяц", "3 месяца", "6 месяцев", name="subscription_duration"), index=True)  # Длительность подписки
    start = Column(Date, index=True)  # Дата начала подписки