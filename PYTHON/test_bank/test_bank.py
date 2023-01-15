from bank import value

def main():
    test_value()


def test_value():
    assert value("Hello") == 0

def test_value():
    assert value("Hi") == 20

def test_value():
    assert value("Morning") == 100

def test_value():
    assert value("HELLO") == 0


if __name__ == "__main__":
    main()