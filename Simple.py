
from itertools import combinations
import pandas as pd
import numpy as np


def Calculation_minimum_support(data):
    mapper = {}
    for i in data:
        for j in i:
            j.lower()
            if j in mapper.keys():
                mapper[j] = mapper[j] + 1
            else:
                mapper[j] = 1
    sum = 0
    for v in mapper.values():
        sum+=v

    res = sum // len(mapper)
    return res,mapper



def clean_the_data(data ,minimum_support,mapper):
    final = []
    for item in data:
        s = ""
        item.sort()
        for items in item:
            if mapper[items] >= minimum_support:
                s += items +","
        final.append(s.split(","))
    return final


def Association_rule(clean_data, items_in_bundle):
    table = {}
    for bundle in clean_data:
        item_combination = list(combinations(bundle, items_in_bundle))
        for k in item_combination:
            if k in table.keys():
                table[k] = table[k] + 1
            else:
                table[k] = 1

    return table


def getSingleUserTransactions(user):
    val = data.loc[data["reviews.username"]==user]["categories"]
    list_of_user_preference = list(val)
    list_of_user_preference_in_different_date = [list(w.split(",")) for w in list_of_user_preference]
    return list_of_user_preference_in_different_date




# data = {"jhon": [["ABOUTL", "BBOLL", "CAT", "D"],
#                  ["CAT", "D", "E"],
#                  ["ABOUTL", "BOLL"],
#                  ["ABOUTL", "CAT", "D"],
#                  ["BBOLL", "D", "F", "G"]],
#
#         "bob": [["A", "B", "F", "E"],
#                 ["C", "F", "E"],
#                 ["A", "C"],
#                 ["A", "C", "D"],
#                 ["B", "E", "F", "G"]]
#         }

data = pd.read_excel('Product Review.xlsx')
user_list = data["reviews.username"].unique()

# for user in user_list:
#     user_transaction = makeFinalDataSet(user)

#     minimum_support, mapper = Calculation_minimum_support(user_transaction)
#     clean_data = clean_the_data(user_transaction, minimum_support,mapper)
#     items_in_bundle = minimum_support+1;
#     count_of_item = Association_rule(clean_data, items_in_bundle)
#     print("{} : {}".format(user, count_of_item))


user = "Abbyks"
user_transaction = getSingleUserTransactions(user)
minimum_support, mapper = Calculation_minimum_support(user_transaction)
clean_data = clean_the_data(user_transaction, minimum_support,mapper)
items_in_bundle = minimum_support+1;
count_of_item = Association_rule(clean_data, items_in_bundle)
print("{} : {}".format(user, count_of_item))