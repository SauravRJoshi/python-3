import csv

class WriteFile:
    def write_detail(self,details):
        with open('student_info.csv' ,'a') as file:
            writer = csv.writer(file)
            writer.writerow(details)
        file.close()
    
    def delete_detail(self,user_inp):
        with open('student_info.csv','r',newline='') as file:
            reader = csv.reader(file)
            lst = list(reader)
            reader_copy = lst.copy()
            for row in reader_copy:
                if row[0] == user_inp:
                    lst.remove(row)
        file.close()

        with open('student_info.csv','w',newline='') as file:
            writer = csv.writer(file)
            for row in lst:
                writer.writerow(row)
        file.close()