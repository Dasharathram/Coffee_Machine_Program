# # creating a dictionary using just the flower brackets
# person = {"name": "James", "country": "Hindustan", "occupation": "Farmer"}
# print(person["occupation"])  # calling with the key
# person["income"] = 1000
# person.update({"phone": 990})
#
# person.update([("weight", 70), ("height", 1.89)])
# # person = {"name": "James", "country": "Hindustan", "occupation": "Farmer"}
# # print(person.keys())
# #
# # person = {"name": "James", "country": "Hindustan", "occupation": "Farmer"}
# # print(person.items())
# #
# # person = {"name": "James", "country": "Hindustan", "occupation": "Farmer"}
# # print(person.values())
# #
# # # creating the dict from dict()
# # student = dict({"name": "James", "country": "Hindustan", "occupation": "Farmer"})
# # print(student)
# #
# # # creating a dict from sequence having them as a pair in tuple (comma "," separated)
# # tourist = dict([("name", "James"), ("country", "Hindustan"), ("occupation", "Farmer")])
# # print(tourist.keys())
# #
# # tourist = dict([("name", "James"), ("country", "Hindustan"), ("occupation", "Farmer")])
# # print(tourist.values())
# #
# # tourist = dict([("name", "James"), ("country", "Hindustan"), ("occupation", "Farmer")])
# # print(tourist.items())  # dict_items([('name', 'James'), ('country', 'Hindustan'), ('occupation', 'Farmer')])
#
# # prints out in a normal manner
# print("key", ":", "value")
# for key in person:
#     print(key, ":", person[key])
#
# for key, value in person.items():
#     print(key, ":", value)
#
# person.setdefault("zip")
# person.setdefault("Married", "Yes")
#
# person.setdefault("occupation", "Engineer")  # no effect at all since we are trying to change the existing value
# print(person)
#
# print(person.pop("Married"))  # removes and returns the value of the key that's passed
#
# print(person.popitem())  # removes and returns the last item in your dict
#
# # print(person.clear())  # removes all the items and returns none
#
# del person["weight"]  # deletes the entire item with that key
# print(person)
#
# # del person  # deletes everything, since the value is gone, there is no name
#
#
# # to check if the key exists use "in"
# key_name = "occupation"
# if key_name in person:
#     print(person[key_name])
#
# dict_2 = {'income': 1001, 'phone': 991, 'height': 1.90}
# person.update(dict_2)
# # print(person)
# dict_1 = {"name": "James", "country": "Hindustan", "occupation": "Farmer"}
# dict_2 = {"income": 1001, "phone": 991, "height": 1.90}
# dictionary = {**dict_2, **dict_1}
# print(dictionary)

# print(full_address)
# print("person:", person)
#
# # retrieve the key in a nested dict
# print(person["address"]["Junction"])
#
# # iterating through the outer dictionary
# for key, value in person.items():
#     if key == "address":
#         for nested_key, nested_value in value.items():
#             print(nested_key, ":", nested_value)
#     else:
#         print(key, ":", value)

full_address = {"Gully": "Oklahoma", "Junction": "Hanuman"}
person = {"name": "James", "country": "Hindustan", "occupation": "Farmer", "address": full_address}
person_husband = {"name": "Jaani", "country": "Hindustan", "occupation": "House Wife", "address": full_address}
person_son = {"name": "Nithin", "country": "Hindustan", "occupation": "student", "address": full_address}

home = {"person_1": person, "person2": person_husband, "person3": person_son}
print(home)

for key, value in home.items():
    print(key)
    for nested_key, nested_value in value.items():
        if nested_key == "address":
            for inward_key, inward_value in full_address.items():
                print(inward_key, ":", inward_value)
            print("\n")
        else:
            print(nested_key, ":", nested_value)
