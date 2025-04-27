from fastapi import FastAPI, HTTPException
from app.models import Task
from app.crud import TaskCRUD

app = FastAPI()
crud = TaskCRUD()

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    return crud.create_task(task)

@app.get("/tasks/", response_model=list[Task])
def list_tasks():
    return crud.list_tasks()

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if crud.delete_task(task_id):
        return {"message": "Task deleted successfully."}
    raise HTTPException(status_code=404, detail="Task not found.")