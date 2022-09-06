import os
import shutil

def add_lesson(class_name, subject_name, lesson):
    file_path = f'./data/{class_name}/subjects/{subject_name}/lessons/{lesson}'

    with open(file_path, 'w') as f:
        pass


def remove_lesson(class_name, subject_name, lesson):
    os.remove(f'./data/{class_name}/subjects/{subject_name}/lessons/{lesson}')

    if subject_name == 'all':
        for folder in os.listdir(f'./data/{class_name}/subjects'):
            shutil.rmtree(f'./data/{class_name}/subjects/{folder}/lessons')
            print('All subjects have been removed.')
    else:
        print(f'Subject {subject_name} does not exist.')