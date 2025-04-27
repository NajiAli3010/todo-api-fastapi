from app.models import Task

class TaskCRUD:
    def __init__(self):
        self.tasks = []

    def create_task(self, task: Task) -> Task:
        self.tasks.append(task)
        return task

    def list_tasks(self) -> list[Task]:
        return self.tasks

    def delete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False