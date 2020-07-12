import sys
class Registration():
	st_id = [0]
	st_dts = []
	info = {}
	rpay = 20000
	def details(self,name,addr,mob,course):
		self.st_dts.append([(self.st_id[-1] + 1),name,addr,mob,course,20000])
		self.info[self.st_id[-1] + 1] = self.rpay
		self.st_id.append(self.st_id[-1] + 1)

	def display_detail(self):
		print(self.st_dts)

	def get_pay(self,no,amount):
		cur_id = self.st_id[no]
		


student = Registration()
student.details("Saurav","Yetkha",9841609896,'IT')
student.display_detail()
student.get_pay(1,10000)