def remove_duplicates (1st): return list(set(1st))

input_list input("Enter a list of values separated by commas: ").split(",")

input_list [int(item) for item in input_list] # Convert input values to integers

=

output_list = remove_duplicates (input_list)

print("Original list:", input_list)

print("List without duplicates: ", output_list)
