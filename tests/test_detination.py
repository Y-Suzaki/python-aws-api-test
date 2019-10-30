from app.srcs.employee import get_list
import pytest


def test_1():
    response = get_list(None, None)
    print("1")
    assert response['statusCode'] == 201


def test_2():
    response = get_list(None, None)
    print("2")
    assert response['statusCode'] == 200


def test_13():
    response = get_list(None, None)
    print("3")
    assert response['statusCode'] == 200


def test_4():
    response = get_list(None, None)
    print("4")
    assert response['statusCode'] == 200


@pytest.mark.parametrize(("num1", "num2", "expect"), [
    (1, 2, 3),
    (1, 2, 3),
    (1, 2, 3),
    (1, 2, 3),
    (3, 4, 7)
])
def test_foo(num1, num2, expect):
    response = get_list(None, None)
    print("5")
    assert response['statusCode'] == 200
