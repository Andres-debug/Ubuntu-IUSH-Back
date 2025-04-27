from fastapi import APIRouter, HTTPException
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate
from app.db.base import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=Item)
def create_item(item: ItemCreate, db: Session = next(get_db())):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = next(get_db())):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate, db: Session = next(get_db())):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/{item_id}", response_model=Item)
def delete_item(item_id: int, db: Session = next(get_db())):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item