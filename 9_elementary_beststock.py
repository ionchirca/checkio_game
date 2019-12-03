#!/usr/bin/python3

import operator
def best_stock(data):
# data.items() - returneaza perechile key:value dintr-un dictionar sub format de lista de tulps [(x, y), (a, b)]
# key=operator.itemgetter(1) - este functia din unctia max() care compara elementele de pe pozitia 1 din lista creata [(x, y), (a, b)], adica y si b in cazul dat
# max() - compara valorile si o returneaza pe cea mai mare
	key = max(data.items(), key=operator.itemgetter(1))[0]
	return key



def best_stock(data):
    return max(data, key=data.__getitem__)
    
if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")
