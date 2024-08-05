def find_max_brute_force(arr):
    if not arr:
        return None  # Handle empty array case
    
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

# Example usage:
arr = [3, 8, 1, 5, 10, 2]
max_element = find_max_brute_force(arr)
print(f"The maximum element in the array is: {max_element}")

