def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    non_duplicates_list = list(set(scores))
    sorted_list = sort_scores_highest_to_lowest(non_duplicates_list)
    return sorted_list[0:3]
    
    
def sort_scores_highest_to_lowest(scores):
    return sorted(scores, reverse = True)
