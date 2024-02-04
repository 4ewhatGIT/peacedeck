import json
import os

def login():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    configs_path = os.path.join(current_dir, "../../configs.json")
    configs_ = open(configs_path, "r", encoding="utf-8")
    configs = json.load(configs_)
    configs_.close()
    del configs_

    users_data_path = os.path.join(current_dir, "users_data.json")
    users_data_ = open(users_data_path, "r", encoding="utf-8")
    users_data = json.load(users_data_)
    users_data_.close()
    del users_data_

    print()
