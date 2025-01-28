class Task:
    def __init__(self, description, priority, id, todos = None):
        self.description = description
        self.priority = priority
        self.completed = False
        self.todos = todos
        self.id = id

    def mark_completed(self):
        self.completed = True

    def delete_task(self):
        if self.todos:
            self.todos.remove(self)        

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"[{self.id}] {self.description} - Priority: {self.priority} - Status: {status}"
    
class ToDo(list):
    def __init__(self, todo=[]):
        super().__init__(todo)

    def __str__(self):
        return f"Tasks:\n\t{'\n\t'.join(str(task) for task in self)}"

    def append(self, task):
        raise AttributeError("Direct use of `append` is not allowed. Use `new_task` instead.")

    def new_task(self, description, priority):
        available_id = max([task.id for task in self], default=0) + 1
        task = Task(description, priority, available_id, self)
        super().append(task)

    def get_task(self, task_id):
        for task in self:
            if task.id == task_id:
                return task
        return None

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            self.remove(task)

    def sort_by_priority(self):
        sorted_tasks = sorted(self, key=lambda task: task.priority)
        return ToDo(sorted_tasks)

    def completed(self):
        return ToDo([task for task in self if task.completed])

    def search(self, keyword):
        return ToDo([task for task in self if keyword.lower() in task.description.lower()])
    
    def mark_all_completed(self):
        new_tasks = ToDo(self)
        for task in new_tasks:
            task.mark_completed()
        return new_tasks

todo = ToDo()

todo.new_task("Buy groceries", 2)
todo.new_task("Finish homework", 2)
todo.new_task("Go for a run", 3)
todo.new_task("Read a book", 1)
todo.new_task("Pay bills", 2)
todo.new_task("Clean the house", 3)
todo.new_task("Call mom", 1)
todo.new_task("Call dad", 3)
todo.new_task("Call Reza", 2)
todo.new_task("Write a report", 2)
todo.new_task("Go to the gym", 3)
todo.new_task("Watch a movie", 1)
todo.new_task("Visit a friend", 2)

todo.get_task(2).mark_completed()
todo.get_task(4).mark_completed()
todo.get_task(6).mark_completed()

todo.get_task(10).delete_task()

print(todo)

print(todo.sort_by_priority())

print(todo.completed().sort_by_priority().search("Read"))

print(todo.search("call").sort_by_priority().mark_all_completed())

print(todo)