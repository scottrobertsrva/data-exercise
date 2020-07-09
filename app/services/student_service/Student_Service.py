from .Student import Student
import csv

class Student_Service:
    def __init__(self, data_file):
        self.data_file = data_file

    def get_students(self):
        with self.data_file.open() as f:
            reader = csv.reader(f, delimiter='_')
            next(reader) # skip header row
            for row in reader:
                yield Student(student_id = row[0], f_name = row[1], 
                                      l_name = row[2], email = row[3],
                                      ssn = row[4], address = row[5],
                                      cid = row[6])
