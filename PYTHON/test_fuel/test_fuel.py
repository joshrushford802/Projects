from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("1/2") == 50
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
    with pytest.raises(ValueError):
        convert("Ronald/McDonald")


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"


if __name__ == "__main__":
    main()