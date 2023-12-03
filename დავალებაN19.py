# B tree
# როდესაც გვინდა დიდი რაოდენობით მონაცემების განთავსება და მოძებნა, ამ შემთხვევაში
# მოუხერხებელი იქნება ჩვეულებრივი binary tree-ს გამოყენება, რადგან ის გაცილებით მეტ ადგილს
# იკავებს მეხსიერებაში და უფრო ნელა მუშაობს, ვიდრე B tree. უკანასკნელი მათგანის კვანძები შეიძლება
# შეიცავდეს ერთზე მეტ key-ს, ამიტომ ამ ხეს ზოგჯერ large key tree-საც უწოდებენ. ამის კარგი მხარე
# ისაა, რომ ხის სიმაღლე მცირდება და ადვილდება მოძებნა. უნდა ითქვას რომ ამ ტიპის ხეში წაშლის,
# ჩამატების და ძებნის Time Complexity თანაბარია-სამივეგან O(log n)-ის ტოლი. n აღნიშნავს ხის ჯამური
# ელემენტების(კვანძების) რაოდენობას.  ყოველ კვანძს, ფოთლების გარდა, ჰყავს key-ზე ერთით მეტი
# შვილი.

class BtreeNode:
    # Btree ხის კვანძი შეიცავს სამ ატრიბუტს-ფოთოლი, გასაღებები და შვილები.
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []


class Btree:
    # t პარამეტრი გამოსახავს მინიმალურ ხარისხს(ხის დონეს)
    def __init__(self, t):
        # ხის ფესვად ვიღებთ BtreeNode კლასის ობიექტს, რომელსაც ფოთოლი აქვს.
        self.root = BtreeNode(True)
        self.t = t

    # ყველას კვანძი შეიცავს მაქსიმუმ (2*t – 1) key-ს.
    def insert(self, k):
        root = self.root
        # თუ ფესვის key-ები გადავსებულია ვამატებთ ახალ კვანძს.
        if len(root.keys) == (2 * self.t) - 1:
            temp = BtreeNode()
            temp.children.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BtreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    def print_tree(self, x, l=0):
        # რეკრუციული ფუნქციის საშუალებით ვბეჭდავთ კვანძის და მისი შვილების გასაღებებს,
        # სანამ შვილების სიგრძე დადებითია.
        print("Level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)

# პირველი პარამეტრი არის გასაღები, მეორე კვანძი.
    def search_key(self, k, x=None):
        if x is not None:
            i = 0
            # თუ x არაა None, მაშინ i იზრდება, თუ x-ის გასაღებების რაოდენობამდე, როცა k მეტია
            # გასაღებების პირველ წევრზე. ეს მეორდება მანამ, სანამ k არ გაუტოლდება რომელიმე k-ს.
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            if i < len(x.keys) and k == x.keys[i][0]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                return self.search_key(k, x.child[i])

        else:
            return self.search_key(k, self.root)