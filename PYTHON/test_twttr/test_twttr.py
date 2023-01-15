from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("Correct") == "Crrct"
    assert shorten("CORRECT") == "CRRCT"

if __name__ == "__main__":
    main()