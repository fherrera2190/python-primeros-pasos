from os import environ
from os import system

userProfile = environ['USERPROFILE']
print(userProfile)

system("start cmd /K cd /d "+userProfile+"")
