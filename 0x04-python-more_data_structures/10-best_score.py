#!/usr/binm/python
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    score = list(a_dictionary.keys())[0]
    initial = a_dictionary[score]
    for key, value in a_dictionary.items():
        if value > initial:
            score = key
            initial = value
    if initial <= 0:
        return None
    return score
