from conftest import *


class TestBun:

    # получаем название булки
    def test_get_name_bun(self, mock_bun):
        assert mock_bun.get_name() == Set1.BUN_NAME

    # получаем стоимость булки
    def test_get_price_bun(self, mock_bun_2):
        assert mock_bun_2.get_price() == Set2.BUN_PRICE
