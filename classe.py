class classes():
    def __init__(profession, name, hp, maxhp, dmg, gold, lvl, exp, max_exp, potki):
        profession.name = name
        profession.hp = hp
        profession.maxhp = maxhp
        profession.dmg = dmg
        profession.gold = gold
        profession.lvl = lvl
        profession.exp = exp
        profession.max_exp = max_exp
        profession.potki = potki

    def __str__(profession) -> str:
        return f"klasa {profession.name}\nhp = {profession.hp}\nmaxhp = {profession.maxhp}\ndmg = {profession.dmg}\ngold = {profession.gold}\nlvl = {profession.lvl}\nexp = {profession.exp}\nmax_exp = {profession.max_exp}\npotki = {profession.potki}"

class1 = classes("Wojownik", 200, 250, 50, 0, 1, 0, 100, 0)
class2 = classes("Alchemik", 100, 150, 50, 0, 1, 0, 100, 3)
class3 = classes("Łotr", 100, 150, 50, 350, 1, 0, 100, 0)
