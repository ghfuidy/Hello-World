# import pip
# import subprocess
# import sys
# import re

# # for dist in pip.get_installed_distributions():
# #     call("pip install --upgrade " + dist.project_name, shell=True)
# reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'list'])

# a = re.findall(r'[A-Za-z]+',str(reqs))
# print(a)

import pip
from pip._internal.utils.misc import get_installed_distributions
from subprocess import call 
for dist in get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)