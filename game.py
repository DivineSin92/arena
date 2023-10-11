import sys, random, time
import items
import classe

#-----------------------------------------------------------------#

def lvl_up():
    if character.exp >= character.max_exp:
        character.lvl += 1
        character.exp = 0
        character.max_exp += 50
        character.maxhp += 50
        character.hp = character.maxhp
        character.dmg += 5
        print(f'Congratulation you reach {character.lvl} lvl! Good Job!')

#-----------------------------------------------------------------#

village = """

1  - Stats
2  - Rest in Tawern
3  - Fight vs week enemy
4  - Fight vs strong enemy
5  - Boss fight
6  - Shell game
7  - Shop
8  - 
9  - 
10 - Exit

"""

print('░█████╗░██████╗░███████╗███╗░░██╗░█████╗░')
print('██╔══██╗██╔══██╗██╔════╝████╗░██║██╔══██╗')
print('███████║██████╔╝█████╗░░██╔██╗██║███████║')
print('██╔══██║██╔══██╗██╔══╝░░██║╚████║██╔══██║')
print('██║░░██║██║░░██║███████╗██║░╚███║██║░░██║')
print('╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝')

print('Welcom in the world when you can just fight vs enemys and not much more just try to have fun and do not die')
print('Now you can choose your class but do it carefully')
print('You can be: ')
time.sleep(1)
print('(1)Strong warrior with more hp')
print('(2)Clever alchemist with potions at start')
print('(3)Sneaky thief with more gold at start')
time.sleep(1)
print('Choose wisely')

class_select = int(input('Select your class: '))
while class_select != 1 or class_select != 2 or class_select != 3:
    if class_select == 1:
        character = classe.class1
        break
    elif class_select == 2:
        character = classe.class2
        break
    elif class_select == 3:
        character = classe.class3
        break
    else:
        print('Sorry but choose existing class')
        class_select = int(input('Select your class: '))

while character.hp>0:
    
    print(village)

    time.sleep(1)

    road_to = int(input('To co robimy?\n'))

    if road_to == 1:
        print('╔' + '═' * 13 + '╦' + '═' * 11 + '╗')
        print('║    name     ║   amount  ║')
        print('╠' + '═' * 13 + '╬' + '═' * 11 + '╣')
        print(f'║     hp      ║  {character.hp:5d}    ║')
        print(f'║    maxhp    ║  {character.maxhp:5d}    ║')
        print(f'║     dmg     ║  {character.dmg:5d}    ║')
        print(f'║    gold     ║  {character.gold:5d}    ║')
        print(f'║     lvl     ║  {character.lvl:5d}    ║')
        print(f'║     exp     ║  {character.exp:5d}    ║')
        print(f'║   max exp   ║  {character.max_exp:5d}    ║')
        print(f'║    potki    ║  {character.potki:5d}    ║')
        print('╚' + '═' * 13 + '╩' + '═' * 11 + '╝')

    elif road_to == 2:
        tawern_cost = character.lvl*20 + random.choice((10, 20, 30))
        if character.gold >= tawern_cost:
            print('So we go sleep. Good Night!')
            print(f'Inkeeper thanks you for {tawern_cost} gold')
            character.gold -= tawern_cost
            character.hp = character.maxhp
        else:
            print('Sorry but you do not have enough gold')

    elif road_to == 3:
        enemy_hp = random.choice((90, 100, 110))
        enemy_dmg = random.choice((10, 20, 30))
        print(f'Your enemy have {enemy_hp} hp and {enemy_dmg} dmg')
        while enemy_hp > 0 and character.hp > 0:
            enemy_hp -= character.dmg
            character.hp -= enemy_dmg
            print(f'Your hp {character.hp} enemy hp {enemy_hp}')
        if enemy_hp <= 0 and character.hp > 0:
            reward_gold = random.choice((10, 20, 30))
            reward_exp = random.choice((20, 30))
            print(f'You win after defeating your enemy you get {reward_gold} gold and {reward_exp} exp')
            character.gold += reward_gold
            character.exp += reward_exp
            lvl_up()

        else:
            if character.potki >= 1:
                print('Potion of immortality save your life')
                character.hp = character.lvl + 5 * 25
                if character.hp > character.maxhp:
                    character.hp = character.maxhp
            else:
                print('You have been defeated your enemy steal all your gold')
                character.hp = character.lvl + 5 * 20
                character.gold = 0
    elif road_to == 4:
        enemy_hp = random.choice((150, 160, 170))
        enemy_dmg = random.choice((40, 50, 60))
        print(f'Your enemy have {enemy_hp} hp and {enemy_dmg} dmg')
        while enemy_hp > 0 and character.hp > 0:
            enemy_hp -= character.dmg
            character.hp -= enemy_dmg
            print(f'Your hp {character.hp} enemy hp {enemy_hp}')
        if enemy_hp <= 0 and character.hp > 0:
            reward_gold = random.choice((40, 50))
            reward_exp = random.choice((40, 50))
            print(f'You win after defeating your enemy you get {reward_gold} gold and {reward_exp} exp')
            character.gold += reward_gold
            character.exp += reward_exp
            lvl_up()
        else:
            if character.potki >= 1:
                print('Potion of immortality save your life')
                character.hp = character.lvl + 5 * 25
                if character.hp > character.maxhp:
                    character.hp = character.maxhp
            else:
                print('You have been defeated your enemy steal all your gold')
                character.hp = character.lvl + 5 * 20
                character.gold = 0
    elif road_to == 5:
        boss_hp_1 = 250
        boss_dmg_1 = 100
        print(f'Boss have {boss_hp_1} hp and {boss_dmg_1} dmg')
        while boss_hp_1 > 0 and character.hp > 0:
            boss_hp_1 -= character.dmg
            character.hp -= boss_dmg_1
            print(f'Your hp {character.hp} enemy hp {boss_hp_1}')
        if boss_hp_1 <= 0 and character.hp > 0:
            rewardg_boss_1 = 100
            rewarde_boss_1 = 100
            print('Your strength is amazing you have defeated powerfull boss')
            print(f'Your reward for this one {rewardg_boss_1} gold and {rewarde_boss_1} exp')
            character.gold += rewardg_boss_1
            character.exp += rewarde_boss_1
            lvl_up()
        else:
            if character.potki >= 1:
                print('Potion of immortality save your life')
                character.hp = character.lvl + 5 * 25
                if character.hp > character.maxhp:
                    character.hp = character.maxhp
            else:
                print('Boss have fun of you and steal all your gold next time train more before fight vs him')
                character.hp = character.lvl + 5 * 20
                character.gold = 0
    elif road_to == 6:
        print('So we playing shell game? Okey')  
        bet = int(input(f'How much gold would you like to bet? You have {character.gold} gold'))
        while bet <= character.gold:
            print('Okey so we have 3 cup 1, 2 and 3 under 1 we have gold and under rest nothing')
            print('Innkeeper start mix cups and now your turn to choose cup')
            cups = [0, 0, 1]
            random.shuffle(cups)
            print('[0, 1, 2]')
            cup_select = int(input('Choose cup: '))
            if cup_select == 0 or cup_select == 1 or cup_select == 2:
                character.gold -= bet
                if cups[cup_select] == 1:
                    character.gold += 2*bet
                    print(f'Congratulation you win this time now you have {character.gold} gold')
                else:
                    print('Not this time Innkeeper win')
                bet_replay = int(input('Do you want to play again?\n1 - Tak\n2 - Nie\n'))
                if bet_replay == 1:
                    print('*Innkeeper have a big smile on his face*')
                    bet = int(input(f'How much gold would you like to bet? You have {character.gold} gold'))
                else:
                    break
            else:
                pass
        if bet > character.gold:
            print('Sorry but you do not have enough gold')
    elif road_to == 7:
        print('Welcom in shop you can buy here new weapon, armor or get a few potions')
        print('1 - Weapons\n2 - Armors\n3 - Potions')
        shop = int(input('What you searching for?\n'))
        if shop == 1:
            print('╔' + 5 * '═' + '╦' + 21 * '═' + '╦' + 7 * '═' + '╦' + 8 * '═' + '╗')
            print('║' + ' id  ' + '║' + '        name        ' + '║' + '  dmg  ' + '║' + '  price  ' + '║')
            print('╠' + 5 * '═' + '╬' + 21 * '═' + '╬' + 7 * '═' + '╬' + 8 * '═' + '╣')
            print(items.sword1)
            print(items.sword2)
            print(items.sword3)
            print(items.sword4)
            print('╚' + 5 * '═' + '╩' + 21 * '═' + '╩' + 7 * '═' + '╩' + 8 * '═' + '╝')
            select = int(input('What do you need?'))
            if select == 1:
                sword = items.sword1
            elif select == 2:
                sword = items.sword2
            elif select == 3:
                sword = items.sword3
            elif select == 4:
                sword = items.sword4
            else:
                print('sorry do not have this item yet')
            if character.gold >= sword.price:
                character.gold -= sword.price
                character.dmg += sword.bdmg
                print('Here you are it is your sword ;)')
            else:
                print('Sorry you do not have enough gold')
        elif shop == 2:
            print('╔' + 5 * '═' + '╦' + 34 * '═' + '╦' + 7 * '═' + '╦' + 8 * '═' + '╗')
            print('║' + ' id  ' + '║' + '              name               ' + '║' + '  hp   ' + '║' + '  price  ' + '║')
            print('╠' + 5 * '═' + '╬' + 34 * '═' + '╬' + 7 * '═' + '╬' + 8 * '═' + '╣')
            print(items.armor1)
            print(items.armor2)
            print(items.armor3)
            print(items.armor4)
            print('╚' + 5 * '═' + '╩' + 34 * '═' + '╩' + 7 * '═' + '╩' + 8 * '═' + '╝')
            select = int(input('What do you need?'))
            if select == 1:
                armor = items.armor1
            elif select == 2:
                armor = items.armor2
            elif select == 3:
                armor = items.armor3
            elif select == 4:
                armor = items.armor4
            else:
                print('sorry do not have this item yet')
            if character.gold >= armor.price:
                character.gold -= armor.price
                character.maxhp += armor.zhp
                print('Here you are it is your armor ;)')
            else:
                print('Sorry you do not have enough gold')
    elif road_to == 10:
        print(':( Good Bye')
        sys.exit()
    else:
        print('Choose something from list!')
