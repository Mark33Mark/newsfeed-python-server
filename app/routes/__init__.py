# the .home syntax directs the program to find the 
# module named home in the current directory. Next, 
# the bp object is imported, we rename it home as 
# part of the import process, for practicality's sake.

from .home import bp as home
from .dashboard import bp as dashboard