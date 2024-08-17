from praktikum.database import Database
from unittest.mock import Mock
from data import *
import pytest


@pytest.fixture
def db():
    return Database()


@pytest.fixture
def mock_bun():
    mock_for_bun = Mock()
    mock_for_bun.get_name.return_value = Set1.BUN_NAME
    mock_for_bun.get_price.return_value = Set1.BUN_PRICE
    return mock_for_bun


@pytest.fixture
def mock_bun_2():
    mock_for_bun_2 = Mock()
    mock_for_bun_2.get_name.return_value = Set2.BUN_NAME
    mock_for_bun_2.get_price.return_value = Set2.BUN_PRICE
    return mock_for_bun_2


@pytest.fixture
def mock_sauce():
    mock_for_sauce = Mock()
    mock_for_sauce.get_name.return_value = Set1.SAUCE_NAME
    mock_for_sauce.get_price.return_value = Set1.SAUCE_PRICE
    mock_for_sauce.get_type.return_value = Set1.SAUCE_TYPE
    return mock_for_sauce


@pytest.fixture
def mock_sauce_2():
    mock_for_sauce_2 = Mock()
    mock_for_sauce_2.get_name.return_value = Set2.SAUCE_NAME
    mock_for_sauce_2.get_price.return_value = Set2.SAUCE_PRICE
    mock_for_sauce_2.get_type.return_value = Set2.SAUCE_TYPE
    return mock_for_sauce_2


@pytest.fixture
def mock_filling():
    mock_for_filling = Mock()
    mock_for_filling.get_name.return_value = Set1.FILLING_NAME
    mock_for_filling.get_price.return_value = Set1.FILLING_PRICE
    mock_for_filling.get_type.return_value = Set1.FILLING_TYPE
    return mock_for_filling


@pytest.fixture
def mock_filling_2():
    mock_for_filling_2 = Mock()
    mock_for_filling_2.get_name.return_value = Set2.FILLING_NAME
    mock_for_filling_2.get_price.return_value = Set2.FILLING_PRICE
    mock_for_filling_2.get_type.return_value = Set2.FILLING_TYPE
    return mock_for_filling_2
