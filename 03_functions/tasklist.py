def add_task(task_dict: dict, task_name: str, done=False):
    task_dict[task_name] = False
    return task_dict

def remove_task(task_dict: dict, task_index: int):
    pass

def print_tasks(task_dict: dict, hide_done=False):
    pass

def mark_done(task_dict: dict, task_index: int):
    pass

def main(task_dict):
    while True:
        print('---[ Tasks ]---')
        print('9: Exit')
        print('1: Print all tasks')
        print('2: Add a task')
        choice = input('Choice: ')
        if choice.startswith('0'):
            break
        if choice.startswith('1')
            print_tasks(task_dict)
        if choice.startswith('2'):
            task_dict = add_task(task_dict, input('Task name: '))
            

main([])