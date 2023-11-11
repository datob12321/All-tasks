# 1. დაწერე ფუნქცია რომელიც მიიღებს ლექსიკონს და ამოშლის მასში ყველა
# დუბლირებულ ინფორმაციას.


# def unique_dict(dict1):
#
#     keys = []
#     values = []
#
#     for k, v in dict1.items():
#         if not v in values:
#             keys.append(k)
#             values.append(v)
#
#     dict1.clear()
#
#     for i in range(len(keys)):
#         dict1[keys[i]] = values[i]
#
#     return dict1
#
# my_dict = {1: 1, 2: 4, 3: 9, 4: 16, -1:1, -2:4, -3:9, -4:16}
# print(unique_dict(my_dict))





# 2. დაწერე ფუნქცია რომელიც მიიღებს ლექსიკონს და შეამოწმებს ცარიელია თუ არა ის
# (დააბრუნებს True თუ ცარიელია ან False_ს თუ არაა ცარიელი.


# def check_dict(dict2):
#     if type(dict2) == dict:
#         if len(dict2) == 0:
#             return True
#         else:
#             return False
#     else:
#         print('pass only dicts to the func, please!')
#
# mydict1 = check_dict({})
# print(mydict1)




# 3. დაწერე ფუნქცია რომელიც მიიღებს სტრიქონის ტიპის მონაცემს, შექმნის მისგან ლექსიკონს
# და დააბრუნებს. (ლექსიკონის გასაღები სტრიქონში არსებული სიმბოლოებია, მნიშვნელობები კი
# განმეორების რაოდენობა.
# მაგ: 'w3schools'
# Expected output: {'w': 1, '3': 1, ‘s': 2, ‘c': 1, ‘h': 1, 'o': 2, ‘l': 1}


# def create_dict(dict3):
#
#     keys = []
#     values = []
#
#     for char in dict3:
#         if not char in keys:
#             keys.append(char)
#             values.append(dict3.count(char))
#
#     my_dict = {}
#     for i in range(len(keys)):
#         my_dict[keys[i]] = values[i]
#     return my_dict
#
# text = "i am a dictionary"
# print(create_dict(text))


# 4. დაწერე ფუნქცია რომელიც მიიღებს ლექსიკონს და დააბრუნებს  ერთ სიაში გაერთიანებულ
# key, value წყვილებს."


# def dict_to_list(dict4):
#     view_object = dict4.items()
#     return view_object
#
# my_dict = {'Italy': 2006, 'Spain': 2010, 'Germany': 2014, 'France': 2018, 'Argentina': 2023}
# print(dict_to_list(my_dict))
