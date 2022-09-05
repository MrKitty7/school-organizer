import os

def add_lesson(class_name, subject_name, lesson):
    file_path = f'./data/{class_name}/subjects/{subject_name}/lessons/{lesson}'

    with open(file_path, 'w') as f:
        pass
    