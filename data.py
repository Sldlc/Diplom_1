from praktikum.ingredient_types import *


class Set1:
    bun_name = 'Флюоресцентная булка R2-D3'
    bun_price = 988

    sauce_type = INGREDIENT_TYPE_SAUCE
    sauce_name = 'Соус Spicy-X'
    sauce_price = 90

    filling_type = INGREDIENT_TYPE_FILLING
    filling_name = 'Мясо бессмертных моллюсков Protostomia'
    filling_price = 1337

    burger_price = bun_price * 2 + sauce_price + filling_price


class Set2:
    bun_name = 'Краторная булка N-200i'
    bun_price = 1255

    sauce_type = INGREDIENT_TYPE_SAUCE
    sauce_name = 'Соус фирменнный Space Sauce'
    sauce_price = 80

    filling_type = INGREDIENT_TYPE_FILLING
    filling_name = 'Говяжий метеорит(отбивная)'
    filling_price = 3000

    burger_price = bun_price * 2 + sauce_price + filling_price


class TestDataBase:
    database_buns = [
        [0, 'black bun', 100],
        [1, 'white bun', 200],
        [2, 'red bun', 300]
    ]

    database_ingredients = [
        [0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100],
        [1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200],
        [2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300],
        [3, INGREDIENT_TYPE_FILLING, 'cutlet', 100],
        [4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200],
        [5, INGREDIENT_TYPE_FILLING, 'sausage', 300]

    ]
