import json
import os.path
import sys

sys.path.append(os.path.join(os.getcwd(), "..\.."))
print(sys.path)

a = open(f"{sys.path[-1]}", "r")

users_data_ = open("users_data.json", "r", encoding="utf-8")
users_data = json.load(users_data_)
del users_data_

print(users_data["default_user"]["name"])
