import sys
from commands.help import help_command
from commands.create_class import create_class
from commands.subject import create_subject
from commands.lesson import add_lesson
from commands.exam import add_exam

# Arguments

# Help Argument
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
        add_exam(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

#------------#