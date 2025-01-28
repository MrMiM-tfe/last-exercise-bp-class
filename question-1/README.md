# Queue System Implementation

A Python implementation of a task queue system with basic queue operations and task management capabilities.

## Features

- Task creation with unique UUID id
- Queue methods (enqueue, dequeue, peek)
- Run tasks in a queue
- Remove tasks by ID

## Usage

```python
# Create a new queue
queue = QueueSystem()

# Create tasks
task_1 = Task("Task 1", "Description 1")
task_2 = Task("Task 2", "Description 2")

# Add tasks to queue
queue.enqueue(task_1)
queue.enqueue(task_2)

# Remove specific task by ID
queue.dequeue(task_2.id)

# Process all tasks in queue
queue.start_queue()
# Queue System Implementation
```

## Explain

### Task :
simple class to create task.
- use `uuid` to generate unique id for each task. to can be used to remove task from queue.
- `__str__` method to print task information.
- `do_task` method to mark task as completed.
```python
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
```

### QueueSystem :
class to create queue system.
- `__init__` method to create queue system.
- `__str__` method to print queue system.
- `enqueue` method to add task to queue.
- `dequeue` method to remove task from queue.
    - `id` is optional, if not provided, the first task in queue will be removed.
- `start_queue` method to run all tasks in queue.

```python
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

```