import json
import os
import importlib.util


def initialize():
    configs_ = open("configs.json", "r", encoding="utf-8")
    language_pack_ = open("system_languages.json", "r", encoding="utf-8")

    configs = json.load(configs_)
    language_pack = json.load(language_pack_)

    configs_.close()
    language_pack_.close()

    del configs_, language_pack_
    UI = language_pack[configs["current_language"]]
    del language_pack

    print(f"{UI['start']} {configs['product_name']} {UI['version']} {configs['version']} ...")


def get_packages(path):
    packages = []
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            packages.append(item)
    return packages


def run_script(package_name, function_name):
    package_path = os.path.join("system_progs", package_name)
    spec = importlib.util.spec_from_file_location("script", os.path.join(package_path, "script.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    getattr(module, function_name)()


packages = get_packages("system_progs")
print("Packages in system_progs: ", packages)
obed = input("module: ")
run_script(obed, "run")
