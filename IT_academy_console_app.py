import sys
import csv

class Registration():
	st_id = [0]
	st_dts = [("ID",'Name',"Address","Mobile Number","Course","Dues")]
	info = {}
	rpay = 20000
	def details(self,name,addr,mob,course):
		self.st_dts.append([(self.st_id[-1] + 1),name,addr,mob,course,self.rpay])
		self.info[self.st_id[-1] + 1] = self.rpay
		self.st_id.append(self.st_id[-1] + 1)

	def get_pay(self,no,amount):
		cur_id = self.st_id[no]
		if amount != 10000 or 20000:
			return print(self.st_dts[cur_id-1][1]," your payment amount is invalid , please pay 10000 or 20000 only .")
		elif self.info[cur_id] == 20000:
			self.info[cur_id] = (self.info[cur_id] - amount)
			self.st_dts[cur_id-1][5] = self.info[cur_id]

	def display_detail(self):
		print(self.st_dts)


	def update_name(self,no,nw_nm):
		cur_id = self.st_id[no]
		self.st_dts[cur_id][1] = nw_nm
	
	def update_addr(self,no,nw_addr):
		cur_id = self.st_id[no]
		self.st_dts[cur_id][2] = nw_addr
	
	def update_mob(self,no,nw_mob):
		cur_id = self.st_id[no]
		self.st_dts[cur_id][3] = nw_mob

	def delete_info(self,no):
		cur_id = self.st_id[no]
		self.st_dts.pop(cur_id-1)

student = Registration()

student.details("Saurav Raj Joshi","Yetkha",9841609896,'Python')
student.details("Fan","Too hot",3,'Spinning')
student.details("Late","Night",12,'Sleeping')
student.display_detail()

student.get_pay(1,10000)
student.get_pay(2,20000)
student.get_pay(3,0)


student.update_name(2,"Pankha")
student.update_mob(3,911)
student.update_addr(2,"Basantpur")


student.delete_info(1)

student.display_detail()


with open('student_info.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(student.st_dts)

f = open('student_info.csv','r')
print(f.read())