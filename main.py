from app_manager import *

if __name__ == "__main__":
    print("start\n")
    Core = Core()
    Core.initialize()
    Core.get_packages_data("system_progs")
