nama_hero = "vramroro"
level = 8
hp = 75.4
is_alive = True
inventory = ["pedang api", "tameng baja", "ramuan beracun"]
atribut = {"kekuatan": 80, "kelincahan": 65}

print("Nama Hero :", nama_hero)
print("Level     :", level)
print("HP        :", hp)
print("Is Alive  :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)

print("Tipe nama_hero :", type(nama_hero))
print("Tipe level     :", type(level))
print("Tipe hp        :", type(hp))
print("Tipe is_alive  :", type(is_alive))
print("Tipe inventory :", type(inventory))
print("Tipe atribut   :", type(atribut))

inventory.append("Ramuan HP")

level = float(level)
level = level + 0.5

print("Nama Hero :", nama_hero)
print("Level     :", level, "->", type(level))
print("HP        :", hp)
print("Is Alive  :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)