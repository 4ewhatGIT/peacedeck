import json

from system_progs import *


def core():
    configs_ = open("configs.json", "r", encoding="utf-8")
    language_pack_ = open("system_languages.json", "r", encoding="utf-8")

    configs = json.load(configs_)
    language_pack = json.load(language_pack_)

    configs_.close()
    language_pack_.close()

    del configs_, language_pack_
    language = language_pack[configs["current_language"]]
    del language_pack

    print(f"{language['start']} {configs['product_name']}...")
