import json
import os
import importlib.util


class Core:
    configs_ = open("configs.json", "r", encoding="utf-8")
    configs = json.load(configs_)
    configs_.close()
    del configs_

    language_pack_ = open("system_languages.json", "r", encoding="utf-8")
    language_pack = json.load(language_pack_)
    language_pack_.close()

    del language_pack_
    UI = language_pack[configs["current_language"]]
    del language_pack

    # Загрузка системы
    def start(self):
        print(f"{Core.UI['start']} {Core.configs['product_name']} {Core.UI['version']} {Core.configs['version']} ...")

    # Получение данных о пакетах
    def get_packages_data(self, path):
        packages_ = []
        for i in os.listdir(path):
            if os.path.isdir(os.path.join(path, i)):
                packages_.append(i)

        packages = {}
        for i in packages_:
            app_info_ = open(f"{path}/{i}/app_info.json", "r", encoding="utf-8")
            app_info = json.load(app_info_)
            app_info_.close()
            del app_info_

            packages[f"{i}"] = {}

            # Получение названия приложения
            is_correct = True  # Корректность app_info.json
            errors = []  # Сбор данных об ошибках (если есть)

            if "title" in app_info:
                if Core.configs["current_language"] in app_info["title"]:
                    packages[f"{i}"]["title"] = app_info["title"][f"{Core.configs['current_language']}"]
                else:
                    if "default" in app_info["title"]:
                        packages[f"{i}"]["title"] = app_info["title"]["default"]
                    else:
                        is_correct = False
                        errors.append(Core.UI["error_receiving_application_data"]["missed_title"])
            else:
                is_correct = False
                errors.append(Core.UI["error_receiving_application_data"]["missed_title"])

            # Получение описания приложения
            if "description" in app_info:
                if Core.configs["current_language"] in app_info["description"]:
                    packages[f"{i}"]["description"] = app_info["description"][f"{Core.configs['current_language']}"]
                else:
                    if "default" in app_info["description"]:
                        packages[f"{i}"]["description"] = app_info["description"]["default"]
                    else:
                        is_correct = False
                        errors.append(Core.UI["error_receiving_application_data"]["missed_description"])
            else:
                is_correct = False
                errors.append(Core.UI["error_receiving_application_data"]["missed_description"])

            # Получение версии приложения
            if "version" in app_info:
                packages[f"{i}"]["version"] = app_info["version"]
            else:
                is_correct = False
                errors.append(Core.UI["error_receiving_application_data"]["missed_version"])

            if is_correct == False:
                packages[f"{i}"]["error"] = errors

        return packages

    # Запуск скрипта пакета
    def run_script(self, package_name, function_name):
        package_path = os.path.join("system_progs", package_name)
        spec = importlib.util.spec_from_file_location("script", os.path.join(package_path, "script.py"))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        getattr(module, function_name)()
