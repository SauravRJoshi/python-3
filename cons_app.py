#!/usr/bin/python3


your_input = 0 
registration = []
std_id = []
std_name = []
std_phone_no = []
std_address = []
std_course_choice = []
payment = []

while your_input != 7:
	print('Your options are : {} {} {} {} {} {} {}'.format("Inquire(1)","Registration(2)","Display(3)","Update(4)","Delete(5)","Return(6)","Exit(7)"))
	your_input = int(input("Enter a choice "))
	if your_input == 1:
		print(""" The course of the study :
			........................
			........................
			........................
			........................""")
	elif your_input == 2:
		print("""Student Registration with Rs. 20000 (deposit). Students are allowed to pay in two installments with Rs. 10000 each.""")
		registration = int(input("Would you like to register : {} {} ".format("yes(1)","no(0)")))
		if registration == 1:
			std_id.append(len(std_id)+1)
			std_name.append(input("Enter your name: "))
			std_phone_no.append(int(input("Enter your phone number: ")))
			std_address.append(input("Enter your address: "))
			std_course_choice.append(input("Enter your choice of course: {} {} {} {} {}".format("Computer Engineering(1)","Electrical Engineering(2)","Civil Engineering(3)","Electronics Enginnering(4)","Archi(5)")))
			current_pay = 0
			print("You have succesfully registered , your remainig dues are : {} ".format('20000'))
			current_pay = int(input("Enter your payment: "))

			if current_pay == 20000:
				print("Thank you for your payment,you have succesfully paid 20000.")
			elif current_pay == 10000:
				pay_yes_no = int(input("You have succesfully paid 10000, would you like to pay again 10000 again : {} {} ".format("yes(1)","no(0)")))
				if pay_yes_no == 1:
					print("Thank you for your payment ,You have succesfully completed your payment")
					current_pay = 20000
				elif pay_yes_no == 0:
					print("Your pending amount is {}, please clear your dues on time ".format(20000-current_pay))

			payment.append(current_pay)
		elif registration == 2:
			print("Thank you")


print(std_name,"\n")
print(std_phone_no,"\n")
print(std_address,"\n")
print(std_course_choice)