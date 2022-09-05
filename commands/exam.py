import os
import datetime

def add_exam(class_name, subject_name, date, exam):
    exam_date = datetime.datetime.strptime(date,"%d/%m/%Y").date()
    today = datetime.date.today()
    remaining = exam_date - today

    path = f'./data/{class_name}/subjects/{subject_name}/exams/{exam}.txt'
    with open(path, 'w') as f:
        f.write(str(exam_date))
    print(f'Remaining days to exam: {remaining.days} days.')