card_no = "5610591081018250"
odd_sum = 0
even_sum = 0
double_list = []
#convert it to list to make iterations
number = list(card_no)
#enumerate to obtain index list
for (idx,val) in enumerate(number):
	if idx %2!=0: #this is an odd number
		odd_sum += int(val)#1.Find the sum of odd index values of the credit card.

	else: #this is the even number 2.Find the number of even numbers.
		double_list.append(int(val)*2)#we enclose the val with bracket or else * will be the priority and will get double value



#converting the list into a string
double_string = ""
for x in double_list:
	double_string += str(x)#3.Calculate the double of even numbers.

#converting the string back to list
double_list = list(double_string)

for x in double_list:
	even_sum += int(x)#4.Find sum of even numbers.

net_sum = odd_sum + even_sum #5.Find sum of odd and even numbers if add up to the multiples of 10 then the credit card is valid.

if net_sum % 10 ==0:
	print('Valid Card')
else:
	print("Invalid Card")
