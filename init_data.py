from database import SessionLocal, engine
from models import FoodItem, DrinkItem, Base

Base.metadata.create_all(bind=engine)


def init_data():
    db = SessionLocal()
    try:
        food_items = [
            FoodItem(name="Pizza Margherita", description="Classic pizza with tomato sauce and mozzarella", price=8.5),
            FoodItem(name="Caesar Salad", description="Fresh romaine lettuce with Caesar dressing", price=6.5),
        ]
        drink_items = [
            DrinkItem(name="Coca Cola", description="Chilled Coca Cola 330ml", price=2.0),
            DrinkItem(name="Red Wine", description="Glass of house red wine", price=4.5),
        ]

        db.bulk_save_objects(food_items)
        db.bulk_save_objects(drink_items)
        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    init_data()
