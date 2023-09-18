import json

configs_ = open("../../configs.json", "r", encoding="utf-8")
configs = json.load(configs_)
del configs_

users_data_ = open("users_data.json", "r", encoding="utf-8")
users_data = json.load(users_data_)
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

print("")
for i in range(len(users_names_list)):
    # TODO: сделать вывод пользователей в таком виде:
    # id: name
    # id: name
    # id: name
    # и так далее...
    print()

