import numpy
import os
import pandas

ID_IDENTIFIER = 'id_'
ATTRIBUTES_FILTER = ['Index', 'penalty']
DEFAULT_DECK = 'amino_acids'
DECKS_PATH = 'decks/{}.csv'


def attr_str(attr):
    if attr in idx:
        return attr[len(ID_IDENTIFIER):]
    else:
        return attr

def val_str(val):
    if type(val) == float:
        return str('%3.3f' % val)
    else:
        return str(val)


def choose_deck():
    print('Topics:')
    decks = [d.split(".")[0] for d in os.listdir('decks/')]
    for deck_name in decks:
        print("    - {}".format(deck_name))
    deck_name = input("Choose deck to learn: [{}] ".format(DEFAULT_DECK))
    if deck_name == "":
        deck_name = DEFAULT_DECK
        print(deck_name)
    if deck_name in decks:
        return deck_name 
    else:
        print("i can't teach you this")


def choose_attributes(item):
    print()
    user_input = input("Do you want to learn all attributes? y/[n] ")
    filtered_fields = list(filter(lambda f: f not in ATTRIBUTES_FILTER, item.keys()))
    if user_input.strip() == "y":
        attributes = filtered_fields
    else:
        print("Please enter 'y' for attributes you want to learn")
        attributes = []
        for attr in filtered_fields:
            if "y" == input("{}: ".format(attr_str(attr))).strip():
                attributes.append(attr)
    print()
    return attributes

def item_by_penalty_dist(items):
    penalties = [i['penalty'] for i in items]
    distribution = [p/sum(penalties) for p in penalties]
    return numpy.random.choice(items, p=distribution)


deck_name = choose_deck()
df = pandas.read_csv(DECKS_PATH.format(deck_name))
idx = list(filter(lambda c: c.startswith(ID_IDENTIFIER), df.columns))
items = df.to_dict(orient='records')


item = item_by_penalty_dist(items)
id_attr = numpy.random.choice(idx)
attributes = choose_attributes(item)

while True:
    # check answers
    print("{}: {}".format(attr_str(id_attr), item[id_attr]))
    answers_correct = {}
    for attr in attributes:
        if attr != id_attr:
            user_input = input("{}: ".format(attr_str(attr)))
            answers_correct[attr] = user_input == val_str(item[attr])
    print()

    # show wrong answers and update penalty
    n_wrong = sum([not(t) for a, t in answers_correct.items()])
    if n_wrong == 0:
        if item["penalty"] > 1: item["penalty"] -= 1
        print('## correct!, penalty:', item["penalty"])
        item = item_by_penalty_dist(items)
        id_attr = numpy.random.choice(idx)
    else:
        print('wrong attributes')
        for attr, truth in answers_correct.items():
            if not(truth):
                print("{}: {}".format(attr_str(attr), val_str(item[attr])))
        item["penalty"] += 2 + n_wrong
        print("## incorrect! penalty:", item["penalty"])

    print('\n-----')

    # save
    df = pandas.DataFrame.from_records(items)
    df.to_csv(DECKS_PATH.format(deck_name), index=False)
