from working import convert
from pytest import raises

def main():
    test_convert()


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    with raises(ValueError):
        convert("9 AM 5 PM")

    with raises(ValueError):
        convert("25 AM to 5 PM")


if __name__ == "__main__":
    main()
