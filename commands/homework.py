import os
import datetime

def add_homework(class_name, subject, homework_name, due_date):
    # Create data folder if it doesn't already exist.
    try:
        os.makedirs('./data')
    except:
        pass
    #------------#

    # Create class folder.
    try:
        os.makedirs(f'./data/{class_name}')
    except:
        pass
    #------------#

    # Create homework folder.
    try:
        os.makedirs(f'./data/{class_name}/homework')
    except:
        pass
    #------------#

    # Create subject folder in homework folder.
    try:
        os.makedirs(f'./data/{class_name}/homework/{subject}')
    except:
        pass
    #------------#

    # Create homework file.
    try:
        file_path = f'./data/{class_name}/homework/{subject}/{homework_name}.txt'
        with open(file_path, 'w') as f:
            today = datetime.date.today()
            lines = [homework_name, today, due_date]
            for line in lines:
                f.write(f'{line}\n')
    
    except:
        pass
    #------------#

    print(f'Homework has been successfully added.')