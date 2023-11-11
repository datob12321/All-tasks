
from collections import defaultdict

მენიუ = {
    'ღორის მწვადი(ერთი შამფური)': 8, 'ხინკალი': 0.5, 'იმერული ხაჭაპური': 5,
           'აჭარული ხაჭაპური': 8, 'ფენოვანი ხაჭაპური': 5, 'ლობიანი': 5, 'ქაბაბი': 3,
           'შემწვარი კარტოფილი': 6, 'ოსტრი': 8, 'შემწვარი ქათამი': 8, 'შემწვარი გოჭი': 30,
           'ლიმონათი': 3, 'წყალი': 1, 'ლუდი': 5
}

კერძები = list(მენიუ.keys())

შეკვეთის_თანხა = 0
შეკვეთილი_კერძები = []
კერძების_რაოდენობა = []


print('   იხილეთ ჩვენი მენიუ.')
print()
print(' 0. შეკვეთის დასრულება')
for i, v in list(enumerate(კერძები)):
    print(rf'{i + 1}. {v} {მენიუ[v]}₾')
print()

while True:
    try:
        შეკვეთა = float(input('შეუკვეთეთ კერძი: '))
        if შეკვეთა == 0:
            break
        elif შეკვეთა in range(1, 15):
            რაოდენობა = int(input('მიუთითეთ რაოდენობა: '))
            if რაოდენობა > 0:
                შეკვეთის_თანხა += მენიუ[კერძები[int(შეკვეთა) - 1]] * რაოდენობა
                if not კერძები[int(შეკვეთა) - 1] in შეკვეთილი_კერძები:
                    კერძების_რაოდენობა.append(რაოდენობა)
                    შეკვეთილი_კერძები.append(კერძები[int(შეკვეთა) - 1])
                else:
                    კერძების_რაოდენობა[კერძების_რაოდენობა.index(რაოდენობა)] += რაოდენობა
            else:
                print('მიუთითეთ დადებითი რაოდენობა!')
    except:
        print('გთხოვთ, აკრიფეთ მხოლოდ რიცხვები!')


zipped = list(zip(შეკვეთილი_კერძები, კერძების_რაოდენობა))
x = ''
for i, v in zipped:
    x += f'{i} - {v} ცალი -- {v*მენიუ[i]}₾\n'


text_to_file = f'''
თქვენ შეუკვეთეთ:

{x}
მთლიანი თანხა - {შეკვეთის_თანხა}₾
'''

def create_file(user_name='User'):
    path = fr'C:\Users\{user_name}\Desktop\check.txt'
    try:
        file = open(path, 'x')
        file.close()
    except FileExistsError:
        print('A file with this name already exists!')
    except:
        print('A directory with such name does not exists!')
    try:
        with open(path, 'w', encoding='utf-16') as f:
            f.write(text_to_file)
            print('The file is successfully created or overwritten on your Desktop!')
    except:
        new_user_name = input('Enter your computer username: ')
        create_file(new_user_name)

create_file()
