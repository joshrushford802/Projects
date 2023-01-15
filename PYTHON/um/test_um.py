from um import count

def main():
    test_count()


def test_count():
    assert count("um") == 1
    assert count("UM") == 1


if __name__ == "__main__":
    main()