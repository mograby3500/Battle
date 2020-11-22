import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4n'

class Person:
    def __init__(self,name, hp, mp, atk, df, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic", "Items"]
        self.items = items


    def generate_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0;

        return  self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return  self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def rduce_mp(self, cost):
        self.mp -= cost

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def choose_action(self):
        i = 1;
        print(bcolors.BOLD +"    " + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE+ bcolors.BOLD + "    ACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE+ bcolors.BOLD + "    MAGIC" + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1


    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "    ITEMS" + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ".", item["item"].name +  ":" , item["item"].description + " (x" + str(item["quantity"]) + ")")
            i += 1

    def choose_target(self, enemies):
        i = 1;
        print("\n" + bcolors.FAIL + bcolors.BOLD + "    Target:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.hp == 0:
                i += 1
                continue

            print("      " + str(i) + ".", enemy.name)
            i += 1
        ch = int(input("    " + self.name + ", Choose Target: ")) - 1
        return  ch



    def get_enemy_stats(self):
        hp_bar = "";
        bar_ticks = (self.hp / self.max_hp) * 100 / 2
        for i in range(int(bar_ticks)):
            hp_bar += "█"

        while len(hp_bar) < 50:
            hp_bar += " "

        n = self.name
        while len(n) < 12:
            n += " "

        chp = str(self.hp)
        while len(chp) < 5:
            chp = "0" + chp;

        mxhp = str(self.max_hp)
        while len(mxhp) < 5:
            mxhp = "0" + mxhp
        cmp = str(self.mp)
        while len(cmp) < 3:
            cmp = "0" + cmp

        print(bcolors.BOLD + n + ":            " +
              chp + "/" + mxhp + " |" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|" + bcolors.ENDC)



    def get_stats(self):
        hp_bar = "";
        bar_ticks = (self.hp/self.max_hp) * 100 / 4

        for i in range(int(bar_ticks)):
            hp_bar += "█"

        while len(hp_bar) < 25:
            hp_bar += " "

        mp_bar = "";
        bar_ticks_mp = (self.mp / self.max_mp) * 100 / 10

        for i in range(int(bar_ticks_mp)):
            mp_bar += "█"

        while len(mp_bar) < 10:
            mp_bar += " "

        chp = str(self.hp)
        while len(chp) < 5:
            chp = "0" + chp;

        mxhp = str(self.max_hp)
        while len(mxhp) < 5:
            mxhp = "0" + mxhp
        cmp = str(self.mp)
        while len(cmp) < 3:
            cmp = "0" + cmp
        print("                                 _________________________                __________")
        print(bcolors.BOLD + self.name + ":            " +
              chp + "/" + mxhp + " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + "|      " + bcolors.BOLD +
              cmp+ "/" + str(self.max_mp) + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")