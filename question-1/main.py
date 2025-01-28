import uuid

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False
        self.id = uuid.uuid4()
    
    def __str__(self):
        return f"Task(name={self.name}, description={self.description}, completed={self.completed})"
    
    def do_task(self):
        self.completed = True

class QueueSystem:
    def __init__(self):
        self.items: list[Task] = []
        self.completed_tasks: list[Task] = []

    def __str__(self):
        return '\n'.join(str(task) for task in self.completed_tasks + self.items)

    def enqueue(self, task):
        """Enqueue a task to the queue."""
        self.items.append(task)

    def dequeue(self, id: uuid.UUID = None):
        """Dequeue a task from the queue."""
        if id is None:
            if len(self.items) > 0:
                return self.items.pop(0)
            else:
                return None
        else:
            for i, task in enumerate(self.items):
                if task.id == id:
                    return self.items.pop(i)
            return None
        
    def peek(self):
        """Peek the next task in the queue."""
        if len(self.items) > 0:
            return self.items[0]
        else:
            return None
        
    def start_queue(self):
        """Start the queue."""
        while len(self.items) > 0:
            task = self.peek()
            task.do_task()
            self.completed_tasks.append(task)
            self.dequeue(task.id)
            print(f"Task '{task.name}' completed.")
        else:
            print("Queue is empty.")

queue_1 = QueueSystem()

task_1 = Task("Task 1", "Description 1")
task_2 = Task("Task 2", "Description 2")
task_3 = Task("Task 3", "Description 3")
task_4 = Task("Task 4", "Description 4")

# enqueue tasks
queue_1.enqueue(task_1)
queue_1.enqueue(task_2)
queue_1.enqueue(task_3)
queue_1.enqueue(task_4)

# dequeue task_2
queue_1.dequeue(task_2.id)

print(queue_1)

queue_1.start_queue()

print(queue_1)