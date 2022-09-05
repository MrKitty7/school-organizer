import os
import shutil

def create_subject(class_name, subject_name):
    # Create data folder if it doesn't already exist.
    try:
        os.makedirs('./data')
    except:
        pass
    #------------#
    
    # Create directories.
    try:
        os.makedirs(f'./data/{class_name}/subjects/{subject_name}')
        os.makedirs(f'./data/{class_name}/subjects/{subject_name}/lessons')
        os.makedirs(f'./data/{class_name}/subjects/{subject_name}/exams')
    except:
        print('Subject already exists.')
    
    print(f'Subject {subject_name} has been successfully created.')

def remove_subject(class_name, subject_name):
    try:
        shutil.rmtree(f'./data/{class_name}/subjects/{subject_name}')
        print(f'Subject {subject_name} has been removed.')
    
    except:
        if subject_name == 'all':
            for folder in os.listdir(f'./data/{class_name}/subjects'):
                shutil.rmtree(f'./data/{class_name}/subjects/{folder}')
        else:
            print(f'Subject {subject_name} does not exist.')