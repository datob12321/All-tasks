# 1

# def triple():
#     text = input("Enter some text: ")
#     print(f"Tripled: {text*3}")
# triple()




# 2

# def weight_on_moon():
#     weight = input("Enter your weight: ")
#     if weight.isdigit():
#         return round(int(weight)/6, 3)
#     else:
#         return "please enter the number"
# print(weight_on_moon())





# 3

# def mini_calc():
#     both_num = True
#     split_symbol = ''
#     nums = []
#     operation = input("enter some math operation using +, -, * or /: ")
#
#     if both_num:
#         for symbol in operation:
#             if not symbol.isdigit() and symbol != ".":
#                 nums = operation.split(symbol)
#                 split_symbol = symbol
#         for i in nums:
#             if i.isalpha():
#                 both_num = False
#         if operation.count(split_symbol) == 1 and operation[0] != split_symbol:
#             if split_symbol == '+':
#                 return float(nums[0])+float(nums[1])
#             elif split_symbol == '-':
#                 return float(nums[0]) - float(nums[1])
#             elif split_symbol == '*':
#                 return float(nums[0]) * float(nums[1])
#             elif split_symbol == '/':
#                 if nums[1] != '0':
#                     return float(nums[0]) / float(nums[1])
#                 else:
#                     return 'Not zero division!'
#             elif split_symbol == '^':
#                 return float(nums[0]) ** float(nums[1])
#             else:
#                 return 'Enter valid operands and symbols!'
#         else:
#             return 'Enter valid operands and symbols!'
#     else:
#         return 'Enter valid operands and symbols!'





# არასავალდებულო დავალება

# def shift():
#     morse = ['•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••', '•---', '-•-',
#              '•-••', '--', '-•', '---', '•--•', '--•-', '•-•', '•••', '-', '••-', '•••-',
#              '•--', '-••-', '-•--', '--••', '  ']
#
#     alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
#                 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
#
#     text = input("Enter some text: ")
#
#     morse_text = ''
#
#     for symbol in text.upper():
#         morse_text += morse[alphabet.index(symbol)]+' '
#     return morse_text






