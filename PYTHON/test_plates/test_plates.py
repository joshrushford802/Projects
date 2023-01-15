from plates import is_valid

def main():
    test_plates()


def test_plates():
    assert is_valid("C") == False
    assert is_valid("CC") == True
    assert is_valid("CCEEDD") == True
    assert is_valid("CCEEDDFFGG") == False
    assert is_valid("CCC555") == True
    assert is_valid("CCC55C") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS!.50") == False


if __name__ == "__main__":
    main()