import random
import amino_acids


DECKS = {"amino acids": amino_acids.data}
DEFAULT_DECK = amino_acids.data

def choose_deck():
    print('Topics:')
    for deck_name in DECKS:
        print("    - {}".format(deck_name))
    deck_name = input("Choose deck to learn: [amino acids] ")
    if deck_name in DECKS:
        return DECKS[deck_name]
    if deck_name  == "":
        return DEFAULT_DECK
    else:
        print("i can't teach you this")

def choose_attributes(item):
    print()
    user_input = input("Do you want to learn all attributes? y/[n] ")
    if user_input.strip() == "y":
        attributes = list(item._fields)
    else:
        print("Please enter 'y' for attributes you want to learn")
        attributes = []
        for attr in item._fields:
            if "y" == input("{}: ".format(attr)).strip():
                attributes.append(attr)
    print()
    return attributes


idx, items = choose_deck()
item = random.choice(items)
identifier = random.choice(idx)
attributes = choose_attributes(item)

while True:
    print(identifier, getattr(item, identifier))
    answers_correct = {}
    for attribute in attributes:
        if attribute != identifier:
            user_input = input("{}: ".format(attribute))
            answers_correct[attribute] = user_input == str(getattr(item, attribute))
    print()
    all_correct = True
    for attribute, truth in answers_correct.items():
        if not(truth):
            if all_correct:
                print('wrong attributes')
                all_correct = False
            print("{}: {}".format(attribute, getattr(item, attribute)))

    if all_correct:
        print('correct!')
        item = random.choice(items)
        identifier = random.choice(idx)
    print('\n-----')

