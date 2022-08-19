import builtins
import main
import yandex_disk
import pytest
import mock

fixture_doc_owner_name = [
    ("2207 876234", "Василий Гупкин"),
    ("11-2", "Геннадий Покемонов"),
    ("10006", "Аристарх Павлов"),
    ("106", None)
]
fixture_all_doc_owners_names = [
    {'Геннадий Покемонов', 'Василий Гупкин', 'Аристарх Павлов'}
]
fixture_add_new_shelf = [
    ("1", False),
    ("2", False),
    ("3", False),
    ("4", True),
]
fixture_delete_doc = [
    ("2207 876234", True),
    ("11-2", True),
    ("10006", True)
]
fixture_get_doc_shelf = [
    ("2207 876234", "1"),
    ("11-2", "1"),
    ("10006", "2"),
    ("1006", None)
]


@pytest.mark.parametrize("a, b", fixture_doc_owner_name)
def test_get_doc_owner_name(a, b):
    with mock.patch.object(builtins, 'input', lambda _: a):
        result = main.get_doc_owner_name()
        assert result == b


@pytest.mark.parametrize("a", fixture_all_doc_owners_names)
def test_get_all_doc_owners_names(a):
    result = main.get_all_doc_owners_names()
    assert result == a


@pytest.mark.parametrize("a, b", fixture_add_new_shelf)
def test_add_new_shelf(a, b):
    with mock.patch.object(builtins, 'input', lambda _: a):
        result = main.add_new_shelf()
        assert result == (a, b)


@pytest.mark.parametrize("a, b", fixture_delete_doc)
def test_delete_doc(a, b):
    with mock.patch.object(builtins, 'input', lambda _: a):
        result = main.delete_doc()
        assert result == (a, b)


@pytest.mark.parametrize("a, b", fixture_get_doc_shelf)
def test_get_doc_shelf(a, b):
    with mock.patch.object(builtins, 'input', lambda _: a):
        result = main.get_doc_shelf()
        assert result == b


fixture_create_folder = [
    ("Новый", 201),
    ("Новый", 409)
]


@pytest.mark.parametrize("a, b", fixture_create_folder)
def test_create_folder(a, b):
    result = yandex_disk.create_folder(a)
    assert result == b
