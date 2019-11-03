# import pip
# from subprocess import call
# from pip._internal.utils.misc import get_installed_distributions
# for dist in get_installed_distributions():
#     call("pip install --upgrade " + dist.project_name, shell=True)

from subprocess import call
    
call("youtube-dl https://www.youtube.com/watch?v=1p6j3xGLtOY&list=PLHOMQ6tK7Yud2RQ38_eF35BtpFY5Hz7qY&index=1")