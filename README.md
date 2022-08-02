# Testing Python Fixtures

This repo contains notes related to some testing libraries for writing test in python.

The main points that were tested here are the following:
1. The interaction of the pytest decorator with unittest patch decorators
2. How the `parameterized` library behave with unittest `TestCase` in comparisson to use regular classes/functions with pytest parametrize decorator.
3. How pytest fixture arguments and mock positional arguments interact in test functions/classes
4. Fixture scope and safe teardown