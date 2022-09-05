import sys
from commands.help import help_command
from commands.create.create_class import create_class

# Arguments

# Help Argument
if sys.argv[1] == 'help':
    help_command()
#------------#

# Create Argument
if sys.argv[1] == 'create':
    if sys.argv[2] == 'class':
        create_class(sys.argv[3])
#------------#