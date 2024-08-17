from conftest import *
from data import *
import pytest


class TestDateFromDB:
    # получаем имя и стоимость булок из базы
    @pytest.mark.parametrize('index_bun, BUN_NAME, BUN_PRICE', TestDataBase.DATABASE_BUNS)
    def test_available_buns_db(self, db, index_bun, BUN_NAME, BUN_PRICE):
        data_buns = db.available_buns()
        assert data_buns[index_bun].get_name() == BUN_NAME
        assert data_buns[index_bun].get_price() == BUN_PRICE

    # получаем имя, стоимость, тип ингредиента из базы
    @pytest.mark.parametrize('index_num, type_ingredient, name_ingredient, price_ingredient',
                             TestDataBase.DATABASE_INGREDIENTS)
    def test_available_ingredients_db(self, db, index_num, type_ingredient, name_ingredient, price_ingredient):
        data_ingredients = db.available_ingredients()
        assert (data_ingredients[index_num].get_name() == name_ingredient and
                data_ingredients[index_num].get_price() == price_ingredient and
                data_ingredients[index_num].get_type() == type_ingredient)
