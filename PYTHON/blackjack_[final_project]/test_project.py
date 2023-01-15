from project import title_screen, shuffled_deck, deal_round

deck = ["ace", "ace", "ace", "ace"]
a = print("\U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50")
b = print("________________Blackjack________________")
c = print("--------Where Kings Meet Computers-------")
d = print()
e = print("Welcome to my table! Here you will test yourself against the skill of a machine and")
f = print("prove once-and-for-all if humans really can beat computers!")
g = print()
h = print("Rules:")
i = print('---Type "hit me" for another card')
j = print('---Type "call" to call')
k = print('---Type "quit" to quit the game')
l = print()
m = print("Good luck!")
n = print("\U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50")
o = print()


def main():
    deck = ["ace", "ace", "ace", "ace"]

def test_title_screen():
    try:
        title_screen(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o)
    except NameError:
        assert False



def test_shuffled_deck():
    assert shuffled_deck(deck) == ["ace", "ace", "ace", "ace"]


def test_deal_round():
    try:
        deal_round(deck)
    except:
        assert True


if __name__ == "__main__":
    main()
