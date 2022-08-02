import pytest
from _pytest.fixtures import FixtureRequest


@pytest.fixture(
    scope="function", # will have its value computed for each function call
    params=[1, -1]    # will produce a different test case for each fixture request, iterating in those values
)
def y(request: FixtureRequest) -> int:
    return request.param

@pytest.fixture(
    scope="module", # will have its value computed once for module (which is each python file)
    # scope="session", # will have its value computed once for the entire test run
)
def z() -> int:
    return 2

    # NOTE # class, module and session scope are great for constant fixtures that do not change across the tests