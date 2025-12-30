from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from ..db import get_session
from ..models import Task
from ..schemas import TaskCreate, TaskUpdate, TaskRead

router = APIRouter()

@router.get("/", response_model=list[TaskRead])
def read_tasks(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    """Get all tasks"""
    statement = select(Task).offset(skip).limit(limit)
    tasks = session.exec(statement).all()
    return tasks

@router.post("/", response_model=TaskRead)
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    """Create a new task"""
    db_task = Task(**task.model_dump())
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@router.put("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task: TaskUpdate, session: Session = Depends(get_session)):
    """Update a task by ID"""
    db_task = session.get(Task, task_id)
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    update_data = task.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@router.delete("/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_session)):
    """Delete a task by ID"""
    db_task = session.get(Task, task_id)
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    session.delete(db_task)
    session.commit()
    return {"message": "Task deleted successfully"}

@router.patch("/{task_id}/complete", response_model=TaskRead)
def toggle_task_complete(task_id: int, completed: bool, session: Session = Depends(get_session)):
    """Toggle task completion status"""
    db_task = session.get(Task, task_id)
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    db_task.completed = completed
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task