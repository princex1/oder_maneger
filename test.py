import json


user_name = input("user_name: ")
password = input('password: ')
city = input('city: ')
input("type ok: ")
# json_ = {user_name: {"user_name": user_name, "password": password, "city": city}}
#
#
# def json1():
#     json_ = {user_name: {"user_name": user_name, "password": password, "city": city}}
#     with open('user_data.json', mode="w") as data:
#         json.dump(json_, data, indent=4)
#
#
# def json2(new_user_entry):
#     try:
#         # seeing if there is any old passwords data file
#         with open("user_data.json", mode="r") as old_password_file:
#             # reading old password data
#             password_data = json.load(old_password_file)
#     # if there is no file or if there is a file but no entries in it:
#     except (FileNotFoundError, json.decoder.JSONDecodeError):
#         with open("user_data.json", mode="w") as new_password_file:
#             json.dump(new_user_entry, new_password_file, indent=4)
#     # if there is old password data,
#     else:
#         #  New user entry json data will be updated to the old passwords data
#         password_data.update(new_user_entry)
#         # Writing either the updated password data or the new user entry json data
#         with open("user_data.json", mode="w") as old_password_file:
#             json.dump(password_data, old_password_file, indent=4)
#
#
# json2(json_)


lists = {"hello": {"name": "prince", "Username": "gohel prince"}, "hello1": {"name": "prince1", "Username": "gohel prince"}}

name = lists[user_name]['name']

print(name)
