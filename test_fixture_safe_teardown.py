
import pytest


class PhantomDB:
    users = []


class User:

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def save(self):
        # Only add user to PhantomDB if no other user has the same name (name is unique)
        if self.name not in [user.name for user in PhantomDB.users]:
            PhantomDB.users.append(self)
        else:
            raise Exception('user already in list')

    def activate(self):
        self.status = 'active'

    def deactivate(self):
        self.status = 'inactive'


@pytest.fixture(scope='function')
def mock_user() -> User:
    user = User(
        name='test_user',
        status='active'
    )
    user.save()

    # return user # uncomment to raise and error in TestUser
    yield user

    # safe teardown code after yield
    PhantomDB.users.pop()

    # NOTE 1. Django TestCase and Rest framework APITestCase run each test inside a db transaction
    # and automatically delete que objects created in the db, so there is no need for a manual teardown
    # NOTE 2. pytest-django has a set of fixtures to achieve the same effect as listed above,
    # and therefore no need for manual teardown for those kinds of db operations.
    # To use it, add the pytest mark decorator: @pytest.mark.django_db (if added to the class, all function will have the desired effect)


class TestUser:

    def test_user_deactivation(self, mock_user: User):
        mock_user.deactivate()
        assert mock_user.status == 'inactive'


    def test_user_activation(self, mock_user: User):
        mock_user.status = 'inactive'
        mock_user.activate()
        assert mock_user.status == 'active'
