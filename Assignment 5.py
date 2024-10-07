def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_list = remove_odd_numbers(original_list)
    print(f"Original list: {original_list}")
    print(f"List with odd numbers removed: {even_list}")

main()
