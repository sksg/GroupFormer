#!/usr/bin/env python3

def list_combinations(input_list, set_count=3):
    total_count = len(input_list)
    if set_count >= total_count:
        yield [input_list]
    
    combination = list(range(set_count))
    while combination[0] < total_count - set_count:
        for low_idx in range(set_count)[::-1]:
            if combination[low_idx] > total_count - (set_count - low_idx):
                combination[low_idx - 1] += 1
                for high_idx in range(low_idx, set_count):
                    combination[high_idx] = combination[high_idx - 1] + 1
            else:
                break
        
        output = [input_list[i] for i in combination]
        remaining_list = [i for i in range(total_count) if i not in combination]
        for remaining_combo in list_combinations(remaining_list, set_count=3):
            yield [output, *remaining_combo]

        combination[-1] += 1


for combination in list_combinations(list(range(10)), 3):
    print(combination)
