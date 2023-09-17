import json


def core():
    configs_ = open("configs.json", "r", encoding="utf-8")
    language_pack_ = open("system_languages.json", "r", encoding="utf-8")
    configs = json.load(configs_)
    language_pack = json.load(language_pack_)
    language = language_pack[configs["current_language"]]
    del configs_, language_pack_, language_pack

    print(f"{language['start']} {configs['product_name']}...")


