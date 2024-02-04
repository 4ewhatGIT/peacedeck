import sys
from os.path import dirname

sys.path.append(dirname(__file__))
import script


def run():
    run = script.Main()
    run.collecting_data()
