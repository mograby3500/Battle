import  random

from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


#Black magic
fire = Spell("Fire", 10, 160, "black")
thunder = Spell("Thunder", 12, 180, "white")
blizzard = Spell("Blizzard", 17, 260, "black")
meteor = Spell("Meteo", 20, 260, "black")
quake = Spell("Quake", 12, 200, "black")


#White magic
cure = Spell("Cure", 12, 1120, "white")
cura = Spell("Cure", 18, 1200, "white")


#create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals for 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals for 500 HP", 500)

elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party memeber", 10000)
hielixer = Item("Mega-Elixer", "elixer", "Fully restores party's HP/MP", 100000)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 10},
                {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 4},
                {"item": hielixer, "quantity": 2},
                {"item": grenade, "quantity": 8}]

player1 = Person("Hazem  ", 3460, 130, 60, 34, player_spells, player_items)
player2 = Person("Hamido ", 4460, 165, 60, 34, player_spells, player_items)
player3 = Person("Azhary ", 2460, 180, 60, 34, player_spells, player_items)


enemy1 = Person("Imp", 1250, 130, 560, 325, [], [])
enemy2 = Person("Big_MONSTER", 12000, 700, 500, 25, [], [])
enemy3 = Person("Imp", 1250, 130, 560, 325, [], [])


players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]


run = True
print(bcolors.FAIL + bcolors.BOLD + "ENEMY ATTACKS" + bcolors.ENDC)

while run:
    print("===================")


    print(bcolors.BOLD + bcolors.OKBLUE + "Name                          HP                                       MP" + bcolors.ENDC)

    print()
    for player in players:
        player.get_stats()

    print()
    for enemy in enemies:
        enemy.get_enemy_stats()

    print()
    for player in players:
        enemy = enemies[player.choose_target(enemies)]
        player.choose_action()
        ch = input("    Choose action: ")
        idx = int(ch) - 1;


        if idx == 0:
            dmg = player.generate_dmg()
            enemy.take_dmg(dmg)
            print("You have made", dmg, "points of damage to " + enemy.name)


        elif idx == 1:
            player.choose_magic()
            mgch = int(input("Choose magic: ")) - 1

            if(mgch == -1):
                continue
            spell = player.magic[mgch]
            magic_dmg = spell.generate_dmg()

            current_mp = player.get_mp()
            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enought mp" + bcolors.ENDC)
                continue

            player.rduce_mp(spell.cost)
            if spell.type == "white":
                prev = player.get_hp()
                player.heal(magic_dmg)
                cur = player.get_hp()

                diff = cur - prev
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(diff) + " HP." + bcolors.ENDC)
            else:
                enemy.take_dmg(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name , "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

        elif idx == 2:
            player.choose_item()
            ch = int(input("    Choose item: ")) - 1

            if ch == -1:
                continue

            if player.items[ch]["quantity"] == 0:
                print(bcolors.FAIL + "This items is not available" + bcolors.ENDC)
                continue

            item = player.items[ch]["item"]
            player.items[ch]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prob)
                print(bcolors.OKGREEN + "\n" + item.name, "Heals for", str(item.prob), "HP", bcolors.ENDC)
            elif item.type == "elixer":
                if item.name == "Mega-Elixer":
                    for i in players:
                        i.hp = i.max_hp
                        i.mp = i.max_mp

                else:
                    player.hp = player.max_hp
                    player.mp = player.max_mp
                print(bcolors.OKGREEN + "\n" + item.name, "fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_dmg(item.prob)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prob), "points of damage" + bcolors.ENDC)



    enemy_dmg = enemies[0].generate_dmg()
    target = random.randrange(0, 3)
    players[target].take_dmg(enemy_dmg)

    defeated_enemies = 0
    defeated_players = 0

    for player in players:
        if player.hp == 0:
            defeated_players += 1


    for enemy in enemies:
        if enemy.hp == 0:
            defeated_enemies += 1

    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "YOU WIN!" + bcolors.ENDC)
        break

    print("Monster made damage", enemy_dmg)
    if defeated_players == 2:
        print(bcolors.FAIL + "YOU LOST,  LOOOSER!" + bcolors.ENDC)
        break


