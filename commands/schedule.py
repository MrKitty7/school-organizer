import os
import shutil

def create_schedule(class_name, schedule_name, day, subject, class_order):
    # Create data folder if it doesn't already exist.
    try:
        os.makedirs('./data')
    except:
        pass
    #------------#

    # Create schedule-name folder.
    try:
        os.makedirs(f'./data/{class_name}/schedule/{schedule_name}')
    except:
        pass
    #------------#

    # Create schedule days folders.
    try:
        os.makedirs(f'./data/{class_name}/schedule/{schedule_name}/monday')
        os.makedirs(f'./data/{class_name}/schedule/{schedule_name}/tuesday')
        os.makedirs(f'./data/{class_name}/schedule/{schedule_name}/wednesday')
        os.makedirs(f'./data/{class_name}/schedule/{schedule_name}/thursday')
        os.makedirs(f'./data/{class_name}/schedule/{schedule_name}/friday')
        os.makedirs(f'./data/{class_name}/schedule/{schedule_name}/saturday')
    
    except:
        pass
    #------------#

    # Create subject folder in schedules folder and file with class_order.
    try:
        os.makedirs(f'./data/{class_name}/schedule/{schedule_name}/{day}/{subject}')
    except:
        pass

    try:
        file_path = f'./data/{class_name}/schedule/{schedule_name}/{day}/{subject}/{class_order}'
        with open(file_path, 'w') as f:
            pass
    
    except:
        pass
    #------------#



    print(f'Schedule has been successfully created.')

def remove_schedule(class_name, schedule_name):
    try:
        shutil.rmtree(f'./data/{class_name}/schedule/{schedule_name}')
        print(f'Schedule {schedule_name} has been removed.')
    
    except:
        if schedule_name == 'all':
            for folder in os.listdir(f'./data/{class_name}/schedule'):
                shutil.rmtree(f'./data/{class_name}/schedule/{folder}')
                print('All schedules have been removed.')
        else:
            print(f'Schedule {schedule_name} does not exist.')

def list_schedule(class_name, schedule_name, day):
    first = ''
    second = ''
    third = ''
    fourth = ''
    fifth = ''
    sixth = ''
    seventh = ''
    eighth = ''
    try:
        for subject_folder in os.listdir(f'./data/{class_name}/schedule/{schedule_name}/{day}'):
            # Open subject folder and list it's files.
            for file in os.listdir(f'./data/{class_name}/schedule/{schedule_name}/{day}/{subject_folder}'):
                if file == '1':
                    first = subject_folder
                if file == '2':
                    second = subject_folder
                if file == '3':
                    third = subject_folder
                if file == '4':
                    fourth = subject_folder
                if file == '5':
                    fifth = subject_folder
                if file == '6':
                    sixth = subject_folder
                if file == '7':
                    seventh = subject_folder
                if file == '8':
                    eighth = subject_folder
    except:
        pass
    
    # Print all.
    print(f'\n 1. {first}\n 2. {second}\n 3. {third}\n 4. {fourth}\n 5. {fifth}\n 6. {sixth}\n 7. {seventh}\n 8. {eighth}')