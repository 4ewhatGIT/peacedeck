from app_manager import *

if __name__ == "__main__":
    print("start\n")
    Core = Core()
    Core.start()
    print(Core.get_packages_data("system_progs"))
    obed = input()
    Core.run_script(obed, "run")