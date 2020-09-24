import csv

class ReadFile:
    def read_st_info(self):
        with open('student_info.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        file.close()
    
    def read_course_info(self):
        with open('course_details.txt', 'r') as file:
            reader = csv.reader(file, delimiter = ' ')
            for row in reader:
                print(row)
        file.close()