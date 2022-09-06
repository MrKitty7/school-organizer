import os
import datetime
import shutil

def add_exam(class_name, subject_name, date, exam):
    exam_date = datetime.datetime.strptime(date,"%d/%m/%Y").date()
    today = datetime.date.today()
    remaining = exam_date - today

    path = f'./data/{class_name}/subjects/{subject_name}/exams/{exam}.txt'
    with open(path, 'w') as f:
        f.write(str(exam_date))
    print(f'Remaining days to exam: {remaining.days} days.')

def remove_exam(class_name, subject_name, exam):
    os.remove(f'./data/{class_name}/subjects/{subject_name}/exams/{exam}.txt')
    print(f'Exam {exam} has been removed.')
    if subject_name == 'all':
        for folder in os.listdir(f'./data/{class_name}/subjects'):
            shutil.rmtree(f'./data/{class_name}/subjects/{folder}/exams')
            print('All subjects have been removed.')
    else:
        print(f'Subject {subject_name} does not exist.')