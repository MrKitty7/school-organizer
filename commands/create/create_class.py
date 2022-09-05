import os
import shutil

def create_class(class_name):
    # Create data folder if it doesn't already exist.
    try:
        os.makedirs('./data')
    except:
        pass
    #------------#
    
    # Create directories.
    try:
        os.makedirs(f'./data/{class_name}')
        os.makedirs(f'./data/{class_name}/subjects')
        os.makedirs(f'./data/{class_name}/exams')
    except:
        print('Class already exists.')
    
    print(f'Class {class_name} has been successfully created.')