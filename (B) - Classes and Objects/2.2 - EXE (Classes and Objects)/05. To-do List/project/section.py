from typing import List
from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []   # [task objects]

    def add_task(self, new_task: Task) -> str:   # new_task == task_object
        if new_task in self.tasks:
            section_name = self.name
            return f"Task is already in the section {section_name}"
        else:
            self.tasks.append(new_task)
            task_details = new_task.details()
            return f"Task {task_details} is added to the section"

    def complete_task(self, task_name: str) -> str:
        task_objects_list = [task_object for task_object in self.tasks
                             if task_object.name == task_name]
        if task_objects_list:
            task_object = task_objects_list[0]
            task_object.completed = True
            return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        completed_task_objects_list = [task_object for task_object in self.tasks
                                       if task_object.completed]   # if task_object.completed == True:
        amount_of_removed_tasks = 0
        for completed_task_object in completed_task_objects_list:
            self.tasks.remove(completed_task_object)
            amount_of_removed_tasks += 1
        return f"Cleared {amount_of_removed_tasks} tasks."

    def view_section(self) -> str:
        section_name = self.name
        details_of_tasks = "\n".join([task_object.details()
                                      for task_object in self.tasks])
        return f"Section {section_name}:" \
               f"\n{details_of_tasks}"
