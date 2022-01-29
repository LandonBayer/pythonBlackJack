import random


class card:
    def __init__(self, suit: str, number: int, name: str) -> None:
        self.suit = suit
        self.number = number
        self.name = name


cardList = []

for i in range(13):
    cardList.append(card("Diamonds", i + 1, ""))
    cardList.append(card("Hearts", i + 1, ""))
    cardList.append(card("Spades", i + 1, ""))
    cardList.append(card("Clubs", i + 1, ""))


def draw(person: list):
    y = len(cardList)
    cardChoice = cardList.pop(random.randint(0, y - 1))
    if cardChoice.number == 10:
        cardChoice.name = "10"
    if cardChoice.number == 11:
        cardChoice.number = 10
        cardChoice.name = "Jack"
    if cardChoice.number == 12:
        cardChoice.number = 10
        cardChoice.name = "Queen"
    if cardChoice.number == 13:
        cardChoice.number = 10
        cardChoice.name = "King"
    person.append(cardChoice)


def royaltyCheck(person: list):
    if person.number == 10:
        return person.name
    else:
        return person.number


def getTotal(person: list):
    personSum = 0
    for i in person:
        personSum = personSum + i.number
    return personSum


def over21(playerTotal: int):
    if playerTotal <= 21:
        print("Your total is", playerTotal)
    else:
        print("Your total is", playerTotal)
        print("Sorry, you lost")
        exit()


player = []
dealer = []

print("Start!")

draw(player)
draw(player)
draw(dealer)
draw(dealer)


print(
    "You have:",
    royaltyCheck(player[0]),
    "of",
    player[0].suit,
    "and",
    royaltyCheck(player[1]),
    "of",
    player[1].suit,
)
print("Dealer has:", royaltyCheck(dealer[0]), "of", dealer[0].suit, "and a facedown")

print("Do you want to hit or stay?")

humanInput = input()

while str(humanInput) == "hit":
    draw(player)
    print("You drew a", player[-1].number, "of", player[-1].suit)
    playerSum = getTotal(player)
    over21(playerSum)
    print("Do you want to hit or stay?")
    humanInput = input()

if str(humanInput) == "stay":
    playerSum = getTotal(player)
    dealerSum = getTotal(dealer)
    print("Your total is", playerSum)
    print("Dealer total is", dealerSum)
    if dealerSum > 21:
        print("Great job! You bust the dealer!")
    elif playerSum <= dealerSum <= 21:
        print("Sorry, you lost")
    while dealerSum < playerSum <= 21:
        print("Dealer is forced to draw...")
        draw(dealer)
        print("They drew a", royaltyCheck(dealer[-1]), "of", dealer[-1].suit)
        dealerSum = getTotal(dealer)
        print("Dealer total is now", dealerSum)
        if dealerSum > 21:
            print("Great job! You bust the dealer!")
        elif playerSum <= dealerSum <= 21:
            print("Sorry, you lost")
