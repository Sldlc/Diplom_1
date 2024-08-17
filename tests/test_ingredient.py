from conftest import *


class TestIngredient:
    # наименование соуса
    def test_get_name_sauce(self, mock_sauce):
        assert mock_sauce.get_name() == Set1.sauce_name

    # стоимость соуса
    def test_get_price_sauce(self, mock_sauce_2):
        assert mock_sauce_2.get_price() == Set2.sauce_price

    # тип ингредиента для соуса
    def test_get_type_sauce(self, mock_sauce):
        assert mock_sauce.get_type() == Set1.sauce_type

    # название начинки
    def test_get_name_filling(self, mock_filling):
        assert mock_filling.get_name() == Set1.filling_name

    # стоимость начинки
    def test_get_price_filling(self, mock_filling_2):
        assert mock_filling_2.get_price() == Set2.filling_price

    # тип ингредиента для начинки
    def test_get_type_filling(self, mock_filling):
        assert mock_filling.get_type() == Set1.filling_type
