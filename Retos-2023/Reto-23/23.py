def calculate_set(first_list, second_list, common):
    common_result = []

    for first_value in first_list:
        if first_value not in common_result:
            for second_value in second_list:
                if first_value == second_value and first_value not in common_result:
                    common_result.append(first_value)
                    break

    if common:
        return common_result
    else:
        non_common_result = []
        non_common_result.extend(first_list)
        non_common_result.extend(second_list)

        for common_value in common_result:
            non_common_result = [x for x in non_common_result if x != common_value]

        return non_common_result

print(calculate_set([1, 2, 3, 3, 4], [2, 2, 3, 3, 3, 4, 6], True))
print(calculate_set([1, 2, 3, 3, 4], [2, 2, 3, 3, 3, 4, 6], False))