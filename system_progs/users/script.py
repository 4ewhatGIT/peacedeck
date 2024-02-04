import json
import os


def run():
    nigga()


def nigga():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    configs_path = os.path.join(current_dir, "../../configs.json")
    configs_ = open(configs_path, "r", encoding="utf-8")
    configs = json.load(configs_)
    configs_.close()
    del configs_

    users_data_ = open("users_data.json", "r", encoding="utf-8")
    users_data = json.load(users_data_)
    users_data_.close()
    del users_data_

    users_names_list = [[f"{users_data['default_user']['name'][configs['current_language']]}",
                         f"{users_data['default_user']['id']}"]]

    if len(list(users_data)) >= 2:
        users_names_list_ = list(users_data)[1:]
        for i in range(len(users_names_list_)):
            users_names_list.append([users_data[users_names_list_[i]]["name"],
                                     users_data[users_names_list_[i]]["id"]])
        del users_names_list_

    # print(users_names_list)  # debug

    language_pack_ = open("languages.json", "r", encoding="utf-8")
    language_pack = json.load(language_pack_)
    language_pack_.close()
    del language_pack_
    UI = language_pack[configs["current_language"]]

    for i in range(len(users_names_list)):
        print(f"{users_names_list[i][1]}. {users_names_list[i][0]}")
    print()
