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
        os.makedirs(f'./data/{class_name}/schedule')
    except:
        print('Class already exists.')
    #------------#
    print(f'Class {class_name} has been successfully created.')

def remove_class(class_name):
    try:
        shutil.rmtree(f'./data/{class_name}')
        print(f'Removed Class {class_name}.')
        
    except:
        if class_name == 'all':
            for folder in os.listdir('data'):
                shutil.rmtree(f'./data/{folder}')
            print('All the classes have been removed.')
        else:
            print(f'Class {class_name} does not exist.')