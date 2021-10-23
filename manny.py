listocars = ['honda civic','miata', 'toyota tacoma', 'BMW 428i']

for cars in listocars:
	if cars == 'BMW 428i':
		print(f"{cars} is a shit car")
	else:
		print(f"{cars} is an amazing car")
		new_car = input("Add a new car to the list dawg")
		listocars.append(new_car)


