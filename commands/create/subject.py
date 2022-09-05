import os

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
    except:
        print('Subject already exists.')
    
    print(f'Subject {subject_name} has been successfully created.')