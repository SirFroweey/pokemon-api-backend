import statistics


def get_average(lst):
    return sum(lst) / len(lst)

def get_mean(lst):
    return statistics.mean(lst)

def get_median(lst):
    return statistics.median(lst)
