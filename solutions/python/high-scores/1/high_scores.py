def latest(scores):
    try:
        return scores[-1]
    except IndexError:
        raise Exception('list index out of range')


def personal_best(scores):
    try:
        return max(scores)
    except ValueError:
        raise Exception('max() is an empty sequence')

def personal_top_three(scores):
    try:
        return sorted(scores, reverse=True)[:3]
    except IndexError:
        raise Exception('list index out of range')
