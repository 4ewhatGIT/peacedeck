from app_manager import *

if __name__ == "__main__":
    print("start\n")
    Core = Core()
    Core.start()
    obed = input()
    Core.run_script(obed, "run")
