def remove_duplicates(lst):
    return list(set(lst))

# Get input from user
lst = input("Enter a list of values, separated by spaces: ").split()

# Convert input values to integers
lst = [int(x) for x in lst]

# Remove duplicates and print result
new_lst = remove_duplicates(lst)
print(new_lst)

