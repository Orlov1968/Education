def apply_all_func(int_list, *functions):
    results = {}
    for i in functions:
        results.update({i.__name__: i(int_list)})
    return results


list_1 = [4, 7, 1, 3]
print(apply_all_func(list_1, sum, min, max, sorted, len))
