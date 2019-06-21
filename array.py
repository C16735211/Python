# array program in python with different features
#
# C16735211 
#
#

numbers = [10,20,300,40.5,50];

# -> we can access a number if we know its index
# print(numbers[0]) will print number 10 at position 0 in the array
print(numbers[0]);

# we now change the number 20 in position 1 in the array to 555
#numbers[1] = 555;

# now when we print the number at position 1 
# we get 555 -> 20 has been updated to 555
#print(numbers[1]);


# now position 2 in the array will hold a string 
#numbers[2] = 'Darren';
#print(numbers[1]);


#for num in numbers:
#	print(num);

#for i in range(len(numbers)):
#	print(numbers[i]);

#print(numbers[0:5]);


# set maximum to the number at position 0 in the array
maximum = numbers[0];

# iterate through the array using num and update the maximum value
for num in numbers:
	if num > maximum:
		maximum = num;

# print the maximum value in the array
print("Maximum: ", maximum);



