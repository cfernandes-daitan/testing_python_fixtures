import math
from unittest import TestCase
from unittest.mock import Mock, patch

import pytest
from parameterized import parameterized


def send_operation_notification(operation_name: str):
    print(f'{operation_name} operation was executed')


def square(x):
    result = math.pow(x, 2)
    send_operation_notification('square')
    return result


def cube(x):
    result = math.pow(x, 3)
    send_operation_notification('cube')

    return result


@patch('testing_python_fixtures.test_patch_and_parametrized_params.send_operation_notification')
class TestSquare:

    @pytest.mark.parametrize("x", [1, 10, 100])
    def test_square(
        self,
        mock_send: Mock, # Class Mock
        x: int # Parametrized arg
    ) -> None:
        assert x*x == square(x)
        mock_send.assert_called_once_with('square')

    @pytest.mark.parametrize("x", [1, 10, 100])
    @patch('math.pow')
    def test_square_special(
        self,
        mock_pow: Mock, # Function Mock
        mock_send: Mock, # Class Mock
        x: int, # Parametrized arg
    ) -> None:
        mock_pow.return_value = x*x # Math's pow function was mocked and its return overwritten
        assert x*x == cube(x)       # That's why the cube function is returning the same value as the square function
                                    # This is just example to illustrate the Mock functionality

        mock_send.assert_called_once_with('cube')

        # NOTE 1. Pytest's parametrize is the outer decorator, and last positional argument, but that's for convinience
        # change the parametrize decorator order does not affect the final result as pytest 'args/fixtures' are named,
        # however its important that they are placed after the mocked arguments

        # NOTE 2. The mock positional arguments follows the order, first function mock, than class mock


@patch('testing_python_fixtures.test_patch_and_parametrized_params.send_operation_notification')
class TestCube(TestCase):

    @parameterized.expand([
        (1,),
        (10,),
        (100,)
    ])
    def test_cube(
        self,
        mock_send: Mock, # Class Mock
        x: int, # Parametrized arg
    ) -> None:
        assert x*x*x == cube(x)
        mock_send.assert_called_once_with('cube')

        # NOTE like with pytest parametrized, the parameterized arg is the last positional argument

    @parameterized.expand([
        (1,),
        (10,),
        (100,)
    ])
    @patch('math.pow')
    def test_cube_special(
        self,
        x: int, # Parametrized arg
        mock_pow: Mock, # Function Mock
        mock_send: Mock, # Class Mock
    ) -> None:
        mock_pow.return_value = x*x*x
        assert x*x*x == square(x)
        mock_send.assert_called_once_with('square')

        # NOTE unlike the previous test, when we add a function mock via patch decorator, eventough the parameterized
        # is the outer decorator, it becomes the first positional argument, which is very unintuitive
