## explain
#### 1. I inherit from list to use all methods in list. an can iterate over it.
```python
class ToDo(list):
    # ...
```

#### 2. Im returning a new list instance to can use multiple methods in row.
```python
def completed(self):
    return ToDo([task for task in self if task.completed])
```

```python
print(todo.completed().sort_by_priority().search("Read"))
```

## how to use it
```python
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
```
### output :
```bash
Tasks:
        [1] Buy groceries - Priority: 2 - Status: Not Completed
        [2] Finish homework - Priority: 2 - Status: Completed
        [3] Go for a run - Priority: 3 - Status: Not Completed
        [4] Read a book - Priority: 1 - Status: Completed
        [5] Pay bills - Priority: 2 - Status: Not Completed
        [6] Clean the house - Priority: 3 - Status: Completed
        [7] Call mom - Priority: 1 - Status: Not Completed
        [8] Call dad - Priority: 3 - Status: Not Completed
        [9] Call Reza - Priority: 2 - Status: Not Completed
        [11] Go to the gym - Priority: 3 - Status: Not Completed
        [12] Watch a movie - Priority: 1 - Status: Not Completed
        [13] Visit a friend - Priority: 2 - Status: Not Completed
Tasks:
        [4] Read a book - Priority: 1 - Status: Completed
        [7] Call mom - Priority: 1 - Status: Not Completed
        [12] Watch a movie - Priority: 1 - Status: Not Completed
        [1] Buy groceries - Priority: 2 - Status: Not Completed
        [2] Finish homework - Priority: 2 - Status: Completed
        [5] Pay bills - Priority: 2 - Status: Not Completed
        [9] Call Reza - Priority: 2 - Status: Not Completed
        [13] Visit a friend - Priority: 2 - Status: Not Completed
        [3] Go for a run - Priority: 3 - Status: Not Completed
        [6] Clean the house - Priority: 3 - Status: Completed
        [8] Call dad - Priority: 3 - Status: Not Completed
        [11] Go to the gym - Priority: 3 - Status: Not Completed
Tasks:
        [4] Read a book - Priority: 1 - Status: Completed
Tasks:
        [7] Call mom - Priority: 1 - Status: Completed
        [9] Call Reza - Priority: 2 - Status: Completed
        [8] Call dad - Priority: 3 - Status: Completed
Tasks:
        [1] Buy groceries - Priority: 2 - Status: Not Completed
        [2] Finish homework - Priority: 2 - Status: Completed
        [3] Go for a run - Priority: 3 - Status: Not Completed
        [4] Read a book - Priority: 1 - Status: Completed
        [5] Pay bills - Priority: 2 - Status: Not Completed
        [6] Clean the house - Priority: 3 - Status: Completed
        [7] Call mom - Priority: 1 - Status: Completed
        [8] Call dad - Priority: 3 - Status: Completed
        [9] Call Reza - Priority: 2 - Status: Completed
        [11] Go to the gym - Priority: 3 - Status: Not Completed
        [12] Watch a movie - Priority: 1 - Status: Not Completed
        [13] Visit a friend - Priority: 2 - Status: Not Completed
```