import os
def list_classes():
    classes = []
    for folder in os.listdir('data'):
        classes.append(folder)
    for folder in classes:
        print(folder)

def list_subjects(class_name):
    subjects = []
    for folder in os.listdir(f'data/{class_name}/subjects'):
        subjects.append(folder)
    for folder in subjects:
        print(folder)

def list_lessons(class_name, subject_name):
    lessons = []
    for folder in os.listdir(f'data/{class_name}/subjects/{subject_name}/lessons'):
        lessons.append(folder)
    for folder in lessons:
        print(folder)

def list_exams(class_name):
    subjects = []
    for folder in os.listdir(f'data/{class_name}/subjects'):
        subjects.append(folder)
    
    for subject in subjects:
        path = f'./data/{class_name}/subjects/{subject}/exams'
        exams = []
        exams.append(os.listdir(path))
        for exam in exams:
            print(str(exam))

def list_homework(class_name, subject_name):
    homework = []
    for file in os.listdir(f'data/{class_name}/homework/{subject_name}'):
        homework.append(file)
    for file in homework:
        with open (f'./data/{class_name}/homework/{subject_name}/{file}', 'r') as f:
            lines = f.readlines()
            print(f'{file} - Due Date: {lines[2]}')
        print(file)