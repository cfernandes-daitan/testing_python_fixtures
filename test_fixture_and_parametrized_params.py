import math
from unittest.mock import Mock, patch

import pytest


def send_operation_notification(operation_name: str):
    print(f'{operation_name} operation was executed')


def _square(x):
    return math.pow(x, 2)


def square_sum(x, y):
    return_value = math.pow(x+y, 2)
    send_operation_notification('square sum')
    return return_value


@pytest.mark.parametrize("x", [10, -10])
def test_square_sum(z:int, x:int, y:int) -> None: # param order does not matter as pytest fixtures are named
    assert square_sum(x, y) == _square(x) + _square(y) + z*(x*y)

    # NOTE fixtures have been defined in conftest.py so it can be share across test modules
    # A fixture defined within a test module/file will be only available in that module/file


@patch('testing_python_fixtures.test_fixture_and_parametrized_params.send_operation_notification')
@pytest.mark.parametrize("x", [10, -10])
def test_square_sum_with_mocked_notification(
    mock_send: Mock, # mocked argument must be placed prior to pytext computed args
    x:int,
    y:int,
    z:int,
) -> None:
    assert square_sum(x, y) == _square(x) + _square(y) + z*(x*y)

    mock_send.assert_called_once_with('square sum')