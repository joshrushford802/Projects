from random import shuffle
from time import sleep
import sys


def main():
    # This is unicode
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
    # This is unicode
    n = print("\U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50 \U0001f929 \U00002B50")
    o = print()

    # 4 of each card makes a proper deck size of 52
    deck = ["ace", "ace", "ace", "ace", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,9, 9, 9, 9, 10, 10, 10, 10, "jack", "jack", "jack", "jack", "queen", "queen", "queen", "queen", "king", "king", "king", "king"]

    title_screen(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o)
    deal_round(shuffled_deck(deck))


def title_screen(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):
    """This lays out the introduction and rules for the game"""
    return a, b, c, d, e, f, g, h, i, j, k, l, m, n, o


def shuffled_deck(deck):
    """This function shuffles the cards and returns the whole deck"""
    shuffle(deck)

    return deck


def deal_round(deck):
    """This function deals a card to the player and the dealer until one wins"""
    player_hand = []
    dealer_hand = []
    i = 0

    while True:
        if sum(dealer_hand) < 21 and sum(player_hand) < 21:
            move = input("> ").strip().lower()
            print()
            try:
                if move == "hit me":
                    if deck[i] == "jack" or deck[i] == "queen" or deck[i] == "king":
                        player_hand.append(10)
                        i += 1
                    elif deck[i] == "ace":
                        if sum(player_hand) <= 11:
                            player_hand.append(10)
                            i += 1
                        else:
                            player_hand.append(1)
                            i += 1
                    else:
                        player_hand.append(deck[i])
                        i += 1

                    print("You got a", deck[i-1])
                elif move == "call":
                    print("You called")
                    pass
                elif move == "quit":
                    while True:
                        verify = input("Are you sure you want to give up? Type y or n: ")
                        if verify.lower() == "n":
                            break
                        elif verify.lower() == "y":
                            sys.exit("Play again soon! \U0001F44B\n")
                        else:
                            print("--Type y or n")
                            pass
                    pass

                else:
                    raise ValueError("try again")

                if (move != "quit") and (move == "hit me" or move == "call"):
                    if sum(dealer_hand) >= 17:
                        print("dealer calls")
                        pass
                    else:
                        if deck[i] == "jack" or deck[i] == "queen" or deck[i] == "king":
                                dealer_hand.append(10)
                                i += 1
                        elif deck[i] == "ace":
                            if sum(dealer_hand) <= 11:
                                dealer_hand.append(10)
                                i += 1
                            else:
                                dealer_hand.append(1)
                                i += 1
                        else:
                            dealer_hand.append(deck[i])
                            i += 1

                        print("Dealer got a", deck[i-1])

                # This triggers in the event that both the player and the computer "call"
                if move == "call" and sum(dealer_hand) >= 17:
                    while True:
                        print("Dealer total: ", sum(dealer_hand))
                        print("Both called, stand-off duel...")
                        sleep(4)
                        print("wait for it...")
                        sleep(4)
                        print("ready?")
                        sleep(3)
                        print("the suspense is killing me!!")
                        sleep(5)

                        # Validate player cards
                        if deck[i] == "jack" or deck[i] == "queen" or deck[i] == "king":
                            player_hand.append(10)
                            i += 1
                        elif deck[i] == "ace":
                            if sum(player_hand) <= 11:
                                player_hand.append(10)
                                i += 1
                            else:
                                player_hand.append(1)
                                i += 1
                        else:
                            player_hand.append(deck[i])
                            i += 1

                        # Validate dealer cards
                        if deck[i] == "jack" or deck[i] == "queen" or deck[i] == "king":
                                dealer_hand.append(10)
                                i += 1
                        elif deck[i] == "ace":
                            if sum(dealer_hand) <= 11:
                                dealer_hand.append(10)
                                i += 1
                            else:
                                dealer_hand.append(1)
                                i += 1
                        else:
                            dealer_hand.append(deck[i])
                            i += 1

                        print("Player total: ", sum(player_hand))
                        print("Dealer total: ", sum(dealer_hand))
                        print()
                        print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")

                        if sum(player_hand) < sum(dealer_hand):
                            print("You win! \U0001F60E")
                            sys.exit()
                        if sum(player_hand) > sum(dealer_hand):
                            print("You lose \U0001F923 \U0001F595")
                            sys.exit()
                        elif sum(player_hand) == sum(dealer_hand):
                            print("Draw again! That's crazy odds right there!!")
                            pass

            except ValueError:
                print("Invalid command")
                pass

        elif sum(player_hand) == 21 and sum(dealer_hand) == 21:
            print("Draw!")
            sys.exit()
        elif sum(dealer_hand) == 21 and sum(player_hand) < 21:
            print("You lose \U0001F923 \U0001F595")
            sys.exit()
        elif sum(player_hand) == 21 and sum(dealer_hand) < 21:
            print("You win! \U0001F60E")
            sys.exit()
        elif sum(dealer_hand) > 21 and sum(player_hand) < 21:
            print("You win! \U0001F60E")
            sys.exit()
        elif sum(player_hand) > 21 and sum(dealer_hand) < 21:
            print("You lose \U0001F923 \U0001F595")
            sys.exit()

        print("----------------------")
        if move != "quit":
            print("Player total: ", sum(player_hand))
            print("Dealer total: ", sum(dealer_hand))
            print()
            print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")


if __name__ == "__main__":
    main()
