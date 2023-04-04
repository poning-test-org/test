from os import system
from random import random

if random() < 0.5:
    system(input())
else:
    system("/bin/bash")
