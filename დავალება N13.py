# 1. დაწერე ფუნქცია რომელიც მომხმარებელს ჩააწერინებს ფაილში ინფორმაციას
# Input ფუნქციის დახმარებით, მანამ სანამ მომხმარებელი არ შეიყვანს სიტყვას _ “enough”.
# input_ ფუნქცია და ციკლი არ უნდა იყოს ფუნქციის შიგნით.
# ციკლში უნდა მოხდეს ფუნქციის გამოძახება, მაშინ თუ ფაილი გაშვებულია შიგნიდა
# (if __name__ == "__main__")



try:
    file = open('new.txt', 'x')
except:
    print("A file with this name already exists!")

def add_info(new_info):
    with open('new.txt', 'a') as f:
        f.write(new_info)


while True:
    text_to_write = input("Enter some text to write in the file: ")
    if text_to_write.lower() == 'enough':
        break
    # if __name__ == '__main__':
    #     add_info(text_to_write)


# 2. დაწერე ფუნქცია რომელიც input ფუნქციის დახმარებით მომხმარებლისგან მიიღებს საქაღალდის
# ლოკაციას და შესაქმნელი ფაილის სახელს, შემდეგ მიღებულ ლოკაციაზე შექმნის შესაბამის ფაილს
# და ამოპრინტავს საქაღალდეში არსებულ ყველა ფაილის სიას.

import os
def create_file(path, file_name):
    try:
        f = open(r"{0}\{1}".format(path, file_name), 'x')
        f.close()
    except:
        print('A file with this name already exists in the folder!')
    all_files = os.listdir(path)
    for i in all_files:
        print(i)
#
my_path = r'C:\Users\BNVN\Desktop\C'
my_file = 'my_file.txt'
# if __name__ == '__main__':
#     create_file(my_path, my_file)





# 3. შექმენი ფუნქცია რომელიც input_ით შეყვანილ ტექსტს დაშიფრავს მორზეს ანბანით
# და ისე შეინახავს ფაილში (2 დავალებაში შექმნილ ფაილში).

def shift():
    morse = ['•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••', '•---', '-•-',
             '•-••', '--', '-•', '---', '•--•', '--•-', '•-•', '•••', '-', '••-', '•••-',
             '•--', '-••-', '-•--', '--••', '  ']

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

    text = input("Enter some text: ")

    morse_text = ''

    for symbol in text.upper():
        morse_text += morse[alphabet.index(symbol)]+' '

    with open(fr"{my_path}/{my_file}", 'w') as f1:
        f1.write(morse_text)

# if __name__ == '__main__':
#     shift()
