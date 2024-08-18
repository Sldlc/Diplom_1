from praktikum.burger import Burger
from conftest import *
import pytest


class TestBurger:
    # добавляем булку в бургер
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # добавляем ингредиенты в бургер; в параметризации проверка с соусом и двумя начинками
    @pytest.mark.parametrize('ingredients, added_ingredient', [
        [Set1.SAUCE_NAME, Set1.SAUCE_NAME],
        [Set1.FILLING_NAME, Set1.FILLING_NAME],
        [Set2.FILLING_NAME, Set2.FILLING_NAME]
        ]
    )
    def test_add_ingredient(self, ingredients, added_ingredient):
        burger = Burger()
        burger.add_ingredient(ingredients)
        assert burger.ingredients == [added_ingredient] and len(burger.ingredients) == 1

    # удаляем ингредиенты из бургера; в параметризации проверка удаления соуса и начинки
    @pytest.mark.parametrize('ingredients, removed_ingredient', [
        [Set1.SAUCE_NAME, Set1.SAUCE_NAME],
        [Set2.FILLING_NAME, Set2.FILLING_NAME]
        ]
    )
    def test_remove_ingredient(self, ingredients, removed_ingredient, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(ingredients)
        burger.remove_ingredient(1)
        assert removed_ingredient not in burger.ingredients and mock_filling in burger.ingredients

    # меняем ингредиенты в бургере
    def test_move_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_filling and burger.ingredients[1] == mock_sauce

    # проверяем цену бургера
    def test_get_price_burger(self, mock_bun_2, mock_sauce_2, mock_filling_2):
        burger = Burger()
        burger.set_buns(mock_bun_2)
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_2)
        assert burger.get_price() == Set2.BURGER_PRICE

    # получаем рецепт бургера и цену бургера
    def test_get_receipt(self, mock_bun, mock_sauce, mock_filling, mock_filling_2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling_2)
        assert burger.get_receipt() == ('(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '= sauce Соус Spicy-X =\n'
                                        '= filling Мясо бессмертных моллюсков Protostomia =\n'
                                        '= filling Говяжий метеорит(отбивная) =\n'
                                        '(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '\n'
                                        f'Price: {burger.get_price()}')
