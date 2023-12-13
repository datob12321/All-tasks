from abc import ABC, abstractmethod
# SOLID

# Single responsibility principle
# ამ პრინციპის აზრი მდგომარეობს იმაში, რომ ერთმა კლასმა უნდა გადაჭრას ერთი ამოცანა. ეს არ
# ნიშნავს იმას, რომ მას მაინცდამაინც ერთი ფუნქცია უნდა ჰქონდეს. კლასს უნდა ევალებოდეს ერთი
# კონკრეტული სახის დავალების შესრულება, რომელიც მოიცავს რამდენიმე მსგავს მეთოდს. მაგ:
# ფაილიდან წაკითხვა და ფაილში ჩაწერა, მონაცემთა სერიალიზაცია და დესერიალიზაცია და ა.შ.შ.


# Open-closed principle
# ამ პრინციპის მიხედვით უნდა გაფართოვდეს კლასის შესაძლებლობები ისე, რომ თვითონ კლასის
# კოდი არ შეიცვალოს. ამის მისაღწევად უმეტესად გამოიყენება აბსტრაქტული კლასები, რომლებიც
# დამემკვიდრებული იქნება ახლადშექმნილი კლასების მიერ. ამ კლასების გამოყენებით გავზრდით
# პროგრამის ფუნქციონალურ შესაძლებობებს.


# Liskov substitution principle
# ეს პრინციპი გვეუბნება, რომ შვილობილი კლასი უნდა მოიქცეს მშობლის მსგავსად და არ უნდა
# შეცვალოს და დაარღვიოს რაიმე წესი მშობელი კლასის მეთოდების გამოძახებისას. ამ პრობლემის
# გადასაჭრელადაც შეგვიძლია მივმართოთ აბსტაქციას, რომელიც აუქმებს იერარქიას შვილობილ
# და მშობელ კლასს შორის. ამგვარად შევძლებთ ორი სხვადასხვა კლასის მეთოდების განსხვავებულად
# ხორცშესხმას ისე, რომ შვილობილ კლასში არ შეიცვალოს მშობელი კლასის იმავე სახელწოდების
# ფუნქცია.


# Interface segregation principle
# ეს პრინციპი გულისხმობს შემდეგს: კლასი არ უნდა შეიცავდეს ისეთ მეთოდებსა და ატრიბუტებს,
# რომლებიც ამ კლასში არ გამოიყენება. ისინი წარმოდგენილი უნდა იყონ რომელიღაც სხვა კლასში.
# შეიძლება გვქონდეს ისეთი შემთხვევა, როცა აბსტრაქტულ კლასს გააჩნდეს მეთოდები, რომლებსაც
# სხვა (A)კლასში განვახორციელებთ, თუმცა ისეთი მეთოდებიც, რომელიც არ გვინდა რომ (A) კლასში
# გვქონდეს. ასეთ მეთოდს შეიძლება იყენებდეს რომელიღაც (B) კლასი, თუმცა-არა (A). ასეთი ამოცანის
# გადაჭრის კარგი გზაა ერთი ინტერფეისის დაყოფა რამდენიმე პატარა ინტერფეისად. ამ დროს ჩვენ
# უკვე შეგვეძლება, რომ კლასებს ის ინტერფეისები დავუმემკვიდროთ, რომელთა მეთოდების
# გამოყენებასაც ვაპირებთ.


# Dependency inversion principle
# ამ პრინციპის თანახმად ერთი კლასი არ უნდა იყოს მეორეზე დამოკიდებული. უნდა არსებობდეს
# ინტერფეისი, რომელზეც იქნება ესა თუ ის კლასი დამოკიდებული.

class Footballer(ABC):
    def __init__(self, name, country, position, total_matches):
        self.name = name
        self.country = country
        self.position = position
        self.total_matches = total_matches

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def average(self):
        pass


class Compare(ABC):
    def __init__(self, player_1: Footballer):
        self.player_1 = player_1

    @abstractmethod
    def compare_matches(self, player_2: Footballer):
        pass


class CompareGoalkeepers(ABC):
    @abstractmethod
    def compare_clean_sheets(self, goalkeeper: Footballer):
        pass


class CompareForwards(ABC):
    @abstractmethod
    def compare_goals(self, forward: Footballer):
        pass





class Goalkeeper(Footballer):
    def __init__(self, name, country, position, total_matches, height, clean_sheets):
        super().__init__(name, country, position, total_matches)
        self.height = height
        self.clean_sheets = clean_sheets

    def get_info(self):
        print(f"{self.name} has {self.clean_sheets} clean_sheets.")

    def average(self):
        return self.clean_sheets / self.total_matches


class Forward(Footballer):
    def __init__(self, name, country, position, total_matches, goals):
        super().__init__(name, country, position, total_matches)
        self.goals = goals

    def get_info(self):
        print(f"{self.name} has {self.goals} goals.")

    def average(self):
        return self.goals / self.total_matches


class CompareToGoalkeeper(Compare, CompareGoalkeepers):
    def __init__(self, goalkeeper: Goalkeeper):
        super().__init__(goalkeeper)

    def compare_matches(self, player_2: Footballer):
        return self.player_1.total_matches - player_2.total_matches

    def compare_clean_sheets(self, goalkeeper: Footballer):
        return self.player_1.clean_sheets - goalkeeper.clean_sheets


class CompareToForward(Compare, CompareForwards):
    def __init__(self, forward: Forward):
        super().__init__(forward)

    def compare_matches(self, player_2: Footballer):
        return self.player_1.total_matches - player_2.total_matches

    def compare_goals(self, forward: Footballer):
        return self.player_1.goals - forward.goals


# S პრინციპი დაცულია რადგან გვაქვს ორი კლასი, რომელთაგან ერთ-ერთი წარმოგვიდგენს
# ზოგად ინფორმაციას ფეხბურთელებზე, მეორე კლასი კი ადარებს ორი ფეხბურთელის
# სხვადასხვა მონაცემებს.
# O პრინციპი ჩანს იმ ნაწილში, რომ ჩვენ შეგვიძლია რომელიმე კლასის კოდის ჩასწორების გარეშე
# გავაფართოვოთ პროგრამის ფუნქციონალი, მაგალითად დავამატოთ ორი კლასი - ნახევარმცველი
# მისთან შედარება. ეს ორივე კლასის შესაბამის ინტერფეისს დაიმემკვიდრებს.
# L პრინციპის მუშაობა იკვეთება კლასების მეთოდებში. ისინი არ ცვლიან მშობელი კლასის
# მეთოდებს(არც ჰყავთ მშობელი კლასი), არამედ მოაქვთ ისინი ინტერფეისიდან.
# I პრინციპის დაცვაშიც ინტერფეისები გვეხმარება. ფეხბურთელთა შედარებისთვის
# გამოყენებულია სამი ინტერფეისი. ერთგან საერთო მეთოდია, ხოლო დანარჩენში - განსხვავებული.
# ასეთი მიდგომის დახმარებით კლასში აღარ გვექნება გამოუყენებელი მეთოდები.
# D პრინციპი შედარებით ნაკლებად იკვეთება მოცემულ კოდში, თუმცა კლასები გარკვეულწილად
# დამოკიდებული არიან ინტერფეისებზე და ნაკლებად ერთმანეთზე.



neuer=Goalkeeper('neuer', 'germany', 'gk', 900,
                 '1.92', 179)
casillas=Goalkeeper('iker', 'spain', 'gk', 960, '1.88', 200)

messi = Forward("Leo", 'Argentina', 'rw', 920, 820)
comp = CompareToGoalkeeper(casillas)
print(comp.compare_clean_sheets(neuer))
comp1 = CompareToForward(messi)
print(comp1.compare_matches(casillas))
