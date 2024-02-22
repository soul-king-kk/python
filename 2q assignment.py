def second_maximum(lst):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[1] if len(sorted_list) > 1 else None

# Example usage:
my_list = [3, 8, 1, 5, 2, 7]
result = second_maximum(my_list)
print(f"The second maximum element in the list is: {result}")