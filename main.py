import sys
from commands.help import help_command
from commands.create.create_class import create_class
from commands.create.subject import create_subject
from commands.add.lesson import add_lesson

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
#------------#