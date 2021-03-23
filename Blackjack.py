from objects import Card, Deck
from db import Money
from datetime import datetime, time
from decimal import Decimal
import locale as lc
import random
from contextlib import closing

def cardCount(cardType):
    points = 0
    if cardType == "Queen" or cardType == "Jack" or cardType == "King":
        points += 10
        return points
    elif cardType == "Ace":
        points += 1
        return points
    else:
        points += cardType
        return points

def main():
    print("Blackjack\n")
    print("Blackjack payout is 3:2\n")
    money = 0.0
    start = datetime.now()
    print("Start time: " + start.strftime("%I:%M:%S %p"))
    result = lc.setlocale(lc.LC_ALL, "")
    if result == "C":
        lc.setlocale(lc.LC_ALL, "en_US")

    while True:
        player = 0
        dealer = 0
        dealerHand = []
        playerHand = []
        
        card = Card()
        deck = Deck(card.getSuits(), card.getRanks())
        deck.shuffle()

        d = deck.getDeck()

        number = random.randint(0, len(d))

        # shows player money, lets them bet and ends if no money
        money = Money()
        money = money.getMoney()
        if money < 5:
            choice = input("Buy more chips? (y/n): ")
            if choice == "y":
                chips = float(input("Enter amount: "))
            elif choice == "n":
                break
        localeMoney = Decimal(money)
        localeMoney = localeMoney.quantize(Decimal("1.00"))
        print("Money: " + lc.currency(localeMoney, grouping=True))
        bet = float(input("Bet amount: "))
        if bet < 5:
            print("Bet must be greater than $5")
            break
        elif bet > 1000:
            print("Bet must be less than $1000")
            break

        # shows dealer card and adds it to dealerHand
        print("DEALER'S SHOW CARD:")
        print(str(d[number][0]) + " of " + d[number][1])
        dealer += cardCount(d[number][0])
        dealerHand.append(d[number])
        d.pop(number)
        print()

        # shows player's cards and adds them to playerHand
        print("YOUR CARDS:")
        for x in range(2):
            number = random.randint(0, len(d))
            print(str(d[number][0]) + " of " + d[number][1])
            player += cardCount(d[number][0])
            playerHand.append(d[number])
            d.pop(number)
        print()

        # determines if blackjack, if not, then player has a chance to hit or stand before dealer
        if dealer == 21:
            print("Dealer blackjack!")
        elif player == 21:
            print("Player blackjack")
        elif player < 21:
            choice = input("Hit or stand? (hit/stand): ")
            print()
            while player < 21 and choice == "hit":
                number = random.randint(0, len(d))
                playerHand.append(d[number])
                player += cardCount(d[number][0])
                d.pop(number)
                print("YOUR CARDS:")
                for x in playerHand:
                    print(str(x[0]) + " of " + x[1])
                print()
                if player > 21:
                    break
                
                choice = input("Hit or stand? (hit/stand): ")

            # Makes dealer draw cards until they have 17 points or until dealer has more points
            while dealer < 17:
                number = random.randint(0, len(d))
                dealerHand.append(d[number])
                dealer += cardCount(d[number][0])

            while dealer < player:
                number = random.randint(0, len(d))
                dealerHand.append(d[number])
                dealer += cardCount(d[number][0])

            # displays both hands and results
            print("DEALER'S CARDS:")
            for x in dealerHand:
                print(str(x[0]) + " of " + x[1])

            print()
            print("YOUR POINTS:\t  " + str(player))
            print("DEALER'S POINTS:  " + str(dealer))
        print()
        with open("money.txt", "w", newline="") as file:
            end = datetime.now()
            if player > 21:
                print("Player busted! House always wins!")
                diff = money - bet
                ph = money
                money = round(money - bet, 2)
                localeMoney = Decimal(money)
                localeMoney = localeMoney.quantize(Decimal("1.00"))
                print("Money: " + lc.currency(localeMoney, grouping=True))
                file.write(str(money))
            elif dealer > 21:
                print("Dealer busted! Cash out, you're done at my tables")
                diff = money - bet
                ph = money
                money = round((bet * 1.5) + money, 2)
                localeMoney = Decimal(money)
                localeMoney = localeMoney.quantize(Decimal("1.00"))
                print("Money: " + lc.currency(localeMoney, grouping=True))
                file.write(str(money))
            elif player <= dealer:
                print("Player lost! Better luck next time, pal!")
                ph = money
                diff = money - bet
                money = round(money - bet, 2)
                localeMoney = Decimal(money)
                localeMoney = localeMoney.quantize(Decimal("1.00"))
                print("Money: " + lc.currency(localeMoney, grouping=True))
                file.write(str(money))

        print()
        choice = input("Play again? (y/n): ")
        if choice == "n":
            end = datetime.now()
            print("Stop time: " + end.strftime("%I:%M:%S %p"))
            hour = end.hour - start.hour
            minute = end.minute - start.minute
            second = end.second - start.second
            print("Elapsed time: " + str(hour) + ":"
                  + str(minute) + ":" + str(second))
            break

if __name__ == "__main__":
    main()
