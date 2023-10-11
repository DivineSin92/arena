class weapon():
    def __init__(sword, id, name, bdmg, price):
        sword.id = id
        sword.name = name
        sword.bdmg = bdmg
        sword.price = price
    def __str__(sword):
        return f"║  {sword.id:1d}  ║  {sword.name:17s}  ║  {sword.bdmg:3d}  ║  {sword.price:4d}  ║"

sword1 = weapon(1, 'Iron sword', 20, 100)
sword2 = weapon(2, 'Epic sword', 40, 200)
sword3 = weapon(3, 'Legendary sword', 50, 400)
sword4 = weapon(4, 'World destroyer sword', 200, 999)

class equipment():
    def __init__(armor, id, name, zhp, price):
        armor.id = id
        armor.name = name
        armor.zhp = zhp
        armor.price = price
    def __str__(armor):
        return f'║  {armor.id:1d}  ║  {armor.name:30s}  ║  {armor.zhp:3d}  ║  {armor.price:4d}  ║'

armor1 = equipment(1, 'Iron armor', 25, 100)
armor2 = equipment(2, 'Epic armor', 50, 200)
armor3 = equipment(3, 'Legendary armor', 100, 400)
armor4 = equipment(4, 'World destroyer armor', 300, 999)
