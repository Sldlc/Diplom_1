from praktikum.ingredient_types import *


class Set1:
    
    BUN_NAME = 'Флюоресцентная булка R2-D3'
    BUN_PRICE = 988

    SAUCE_TYPE = INGREDIENT_TYPE_SAUCE
    SAUCE_NAME = 'Соус Spicy-X'
    SAUCE_PRICE = 90

    FILLING_TYPE = INGREDIENT_TYPE_FILLING
    FILLING_NAME = 'Мясо бессмертных моллюсков Protostomia'
    FILLING_PRICE = 1337

    BURGER_PRICE = BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE


class Set2:
    
    BUN_NAME = 'Краторная булка N-200i'
    BUN_PRICE = 1255

    SAUCE_TYPE = INGREDIENT_TYPE_SAUCE
    SAUCE_NAME = 'Соус фирменнный Space Sauce'
    SAUCE_PRICE = 80

    FILLING_TYPE = INGREDIENT_TYPE_FILLING
    FILLING_NAME = 'Говяжий метеорит(отбивная)'
    FILLING_PRICE = 3000

    BURGER_PRICE = BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE


class TestDataBase:
    
    DATABASE_BUNS = [
        [0, 'black bun', 100],
        [1, 'white bun', 200],
        [2, 'red bun', 300]
    ]

    DATABASE_INGREDIENTS = [
        [0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100],
        [1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200],
        [2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300],
        [3, INGREDIENT_TYPE_FILLING, 'cutlet', 100],
        [4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200],
        [5, INGREDIENT_TYPE_FILLING, 'sausage', 300]

    ]
