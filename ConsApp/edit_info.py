import csv

class Edit_file:

    def edit_info(self,roll,user_inp,val):
        with open('student_info.csv','r',newline='') as file:
            reader = csv.reader(file)
            lst = list(reader)
            reader_copy = lst.copy()
            for row in reader_copy:
                if row[0] == roll:
                    if val == 1:
                        row[1] = user_inp
                    elif val == 2:
                        row[2] = user_inp
                    elif val == 3:
                        row[3] = user_inp
        file.close()

        with open('student_info.csv','w',newline='') as file:
            writer = csv.writer(file)
            for row in reader_copy:
                writer.writerow(row)
        file.close()


test = Edit_file()
test.edit_info('1','SRJ',1)