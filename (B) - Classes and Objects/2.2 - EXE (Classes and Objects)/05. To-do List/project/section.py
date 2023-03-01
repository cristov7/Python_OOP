from project.task import Task
from typing import List


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        try:
            task_info = [task for task in self.tasks if task.name == task_name][0]
            task_info.completed = Task
            return f"Completed task {task_name}"
        except IndexError:
            return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        amount_of_removed_tasks = len(self.tasks)
        self.tasks.clear()
        return f"Cleared {amount_of_removed_tasks} tasks."

    def view_section(self) -> str:
        details_of_tasks = "\n".join([task.details() for task in self.tasks])
        return f"Section {self.name}:" \
               f"\n{details_of_tasks}"
