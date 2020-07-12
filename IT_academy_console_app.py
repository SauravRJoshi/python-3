import sys
class Registration():
	st_id = [0]
	st_dts = []
	info = {}
	rpay = 20000
	def details(self,name,addr,mob,course):
		self.st_dts.append([(self.st_id[-1] + 1),name,addr,mob,course,self.rpay])
		self.info[self.st_id[-1] + 1] = self.rpay
		self.st_id.append(self.st_id[-1] + 1)

	def get_pay(self,no,amount):
		cur_id = self.st_id[no]
		if self.info[cur_id] == 20000:
			self.info[cur_id] = (self.info[cur_id] - amount)
			self.st_dts[cur_id-1][5] = self.info[cur_id]

	def display_detail(self):
		print(self.st_dts)


	def update_name(self,no,nw_nm):
		cur_id = self.st_id[no]
		self.st_dts[cur_id-1][1] = nw_nm
	
	def update_addr(self,no,nw_addr):
		cur_id = self.st_id[no]
		self.st_dts[cur_id-1][2] = nw_addr
	
	def update_mob(self,no,nw_mob):
		cur_id = self.st_id[no]
		self.st_dts[cur_id-1][3] = nw_mob


student = Registration()

# a = 0
# while a != 8:
# 	a = input("Enter a number ")
# 	if a == 1:
# 		nm = input("Enter name")
# 		addr = input("Enter address")
# 		mob = input("Enter mobile number")
# 		cour = input("Enter course")
# 		# student.details("Saurav","Yetkha",9841609896,'IT')
# 		student.details(nm,addr,mob,cour)
# 	elif a == 2:
# 		student.get_pay(1,10000)
# 	elif a == 3:
# 		student.update_name(1,"DonDai")
# 		student.update_addr(1,"China")
# 		student.update_mob(1,352385)
# 	elif a == 4:
# 		student.display_detail()

	
student.details("Saurav","Yetkha",9841609896,'IT')
student.display_detail()
student.get_pay(1,10000)
student.update_name(1,"DonDai")
student.update_addr(1,"China")
student.update_mob(1,352385)
student.display_detail()


