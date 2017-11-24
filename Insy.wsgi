import sys
sys.path.insert(0,"/Users/akmalfadlurohman/Documents/Code/Python/Insy")

activate_this = '/Users/akmalfadlurohman/Documents/Code/Python/Insy/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from insy_app import app as application