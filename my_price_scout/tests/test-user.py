import pytest

from files.user import User


def test_get_item(mock_item_1, mock_user):
    mock_user.watchlist.append(mock_item_1)

    actual_item = mock_user.get_item(mock_item_1.name)

    assert actual_item == mock_item_1


def test_add_item(mock_item_1, mock_user):
    assert len(mock_user.watchlist) == 0

    mock_user.add_item(mock_item_1)

    assert len(mock_user.watchlist) == 1
    assert mock_user.watchlist[0] == mock_item_1


def test_remove_item(mock_item_1, mock_user):
    mock_user.watchlist.append(mock_item_1)
    mock_user.remove_item(mock_item_1.name)

    assert len(mock_user.watchlist) == 0


def test_replace_item(mock_item_1, mock_item_2, mock_user):
    mock_user.watchlist.append(mock_item_1)
    mock_user.replace_item(mock_item_1.name, mock_item_2)

    assert mock_user.watchlist[0] == mock_item_2


def test_get_watchlist(mock_item_1, mock_item_2, mock_user):
    mock_user.watchlist.append(mock_item_1)
    mock_user.watchlist.append(mock_item_2)

    items = mock_user.get_watchlist()

    assert items[0] == mock_item_1
    assert items[1] == mock_item_2


@pytest.fixture
def mock_item_1():
    class MockItem(object):
        name = "mock item 1"
    return MockItem()


@pytest.fixture
def mock_item_2():
    class MockItem(object):
        name = "mock item 2"
    return MockItem()


@pytest.fixture
def mock_user():
    return User("mock email", "mock phone number", "mock cell carrier")
