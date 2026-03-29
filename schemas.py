from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.dependencies import get_db, get_current_user
from app.dependencies import admin_required
from fastapi import HTTPException

router = APIRouter()

@router.post("/tasks")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_task = models.Task(
        title=task.title,
        description=task.description,
        owner_id=user.id
    )
    db.add(new_task)
    db.commit()
    return {"message": "Task created"}

@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(models.Task).filter(models.Task.owner_id == user.id).all()

@router.delete("/admin/tasks/{task_id}")
def admin_delete_task(task_id: int, db: Session = Depends(get_db), user=Depends(admin_required)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"message": "Deleted by admin"}\

@router.get("/admin/tasks")
def get_all_tasks(db: Session = Depends(get_db), user=Depends(admin_required)):
    return db.query(models.Task).all()

@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: schemas.TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.owner_id != user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    task.title = updated_task.title
    task.description = updated_task.description

    db.commit()
    return {"message": "Task updated"}