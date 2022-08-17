# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

# Step 2: write a line of code that removes the last element from the list.

# Step 3: write a line of code that prints the length of the existing list.

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
print(hat_list)

numbers= int(input("Pick up a number: "))
hat_list[2]= numbers

del hat_list[4]
print("List lenght: ", len(hat_list))

print(hat_list)

