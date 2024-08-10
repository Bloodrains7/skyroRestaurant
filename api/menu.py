from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import FoodItem, DrinkItem
from fastapi.responses import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
import os

router = APIRouter()


def generate_pdf(filename, title, items):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Add title
    elements.append(Paragraph(title, styles['Title']))

    # Create table data
    data = [["Name", "Description", "Price"]]
    for item in items:
        data.append([item.name, item.description, f"${item.price:.2f}"])

    # Create table
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    # Build PDF
    doc.build(elements)


@router.get("/menu/food")
def get_food_menu(db: Session = Depends(get_db)):
    food_items = db.query(FoodItem).all()
    filename = "food_menu.pdf"
    generate_pdf(filename, "Food Menu", food_items)

    if not os.path.exists(filename):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(filename, media_type='application/pdf', filename=filename)


@router.get("/menu/drinks")
def get_drinks_menu(db: Session = Depends(get_db)):
    drink_items = db.query(DrinkItem).all()
    filename = "drinks_menu.pdf"
    generate_pdf(filename, "Drinks Menu", drink_items)

    if not os.path.exists(filename):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(filename, media_type='application/pdf', filename=filename)
