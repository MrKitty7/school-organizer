import sys
from commands.help import *
from commands.create_class import *
from commands.exam import *
from commands.lesson import *
from commands.subject import *
from commands.list import *

# Arguments

if sys.argv[1] == 'help':
    help_command()
#------------#

# Create Argument
if sys.argv[1] == 'create':
    if sys.argv[2] == 'class':
        create_class(sys.argv[3])
    if sys.argv[2] == 'subject':
        create_subject(sys.argv[3], sys.argv[4])
#------------#

# Add Argument
if sys.argv[1] == 'add':
    if sys.argv[2] == 'lesson':
        add_lesson(sys.argv[3], sys.argv[4], sys.argv[5])
    if sys.argv[2] == 'exam':
        add_exam(sys.argv[3], sys.argv[4], sys.argv[5],  sys.argv[6])

#------------#

# List Argument
if sys.argv[1] == 'list':
    if sys.argv[2] == 'classes':
        list_classes()
    if sys.argv[2] == 'subjects':
        list_subjects(sys.argv[3])
    if sys.argv[2] == 'lessons':
        list_lessons(sys.argv[3], sys.argv[4])
    if sys.argv[2] == 'exams':
        list_exams(sys.argv[3])

# Remove Argument
if sys.argv[1] == 'remove':
    if sys.argv[2] == 'class':
        remove_class(sys.argv[3])
    if sys.argv[2] == 'subject':
        remove_subject(sys.argv[3], sys.argv[4])