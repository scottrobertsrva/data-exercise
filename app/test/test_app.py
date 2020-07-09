import unittest
from pathlib import Path
import csv
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import json

from report import Report
from services import student_service
from services import teacher_service

class TestReportApp(unittest.TestCase):
    def setUp(self):
        # files setup
        data_folder = 'test_data'
        student_filename = 'students.csv'
        teacher_filename = 'teachers.parquet'
        output_folder = 'test_output'
        output_filename = 'report.json'
        root_dir = Path(__file__, '..')
        self.student_data = root_dir / data_folder / student_filename
        self.teacher_data = root_dir / data_folder / teacher_filename
        self.output_file = root_dir / output_folder / output_filename

        # generate test data
        students = [
            'id_fname_lname_email_ssn_address_cid',
            '1_Dniren_Dewbury_ddewbury0@illinois.edu_498-19-2152_63083 Jana Point_1',
            '2_Marten_Catanheira_mcatanheira1@nyu.edu_734-61-0692_7 Lawn Alley_2',
            '3_Shae_Olivet_solivet2@guardian.co.uk_633-18-3236_5 Golf View Alley_3'
        ]

        teachers = [['10', 'Jessa', 'Gibbs', 'jgibbs0@bandcamp.com', '733-04-9225', '32 Ridgeview Circle', '3'],
                        ['11', 'Tate', 'Weekley', 'tweekley1@nps.gov', '392-55-5726', '5 Lawn Alley', '2'],
                        ['12', 'Trenna', 'Chasney', 'tchasney2@vimeo.com', '608-97-4356', '4 Sunbrook Crossing', '1']
                       ]

        with open(self.student_data.resolve(), 'w+') as f:
            for student in students:
                f.write(student)
                f.write('\n')


        df = pd.DataFrame(teachers, columns = ['id', 'fname', 'lname', 'email', 'ssn', 'address', 'cid']) 
        table = pa.Table.from_pandas(df)
        pq.write_table(table, self.teacher_data.resolve())

        # instantiate objects
        self.student_service = student_service.Student_Service.Student_Service(self.student_data)
        self.teacher_service = teacher_service.Teacher_Service.Teacher_Service(self.teacher_data)
        self.report = Report(self.teacher_service, self.student_service, self.output_file)


    def test_student_service_get_students(self):
        student_generator = self.student_service.get_students()
        students = []
        for student in student_generator:
            students.append(student)
        # check last student first name
        self.assertEqual(students[2].f_name, 'Shae')

    def test_teacher_service_get_teacher(self):
        teacher = self.teacher_service.get_teacher('3')
        # check teacher cid
        self.assertEqual(teacher.cid, '3')

    def test_report_record_count(self):
        self.report.write_report()
        data = None
        with open(self.output_file.resolve()) as f:
            data = json.load(f)
        # file should have 3 records from test data
        self.assertEqual(len(data), 3)

    def test_report_data(self):
        self.report.write_report()
        data = None
        with open(self.output_file.resolve()) as f:
            data = json.load(f)
        # check last record for correct teacher first name
        self.assertEqual(data[2]['teacher_f_name'], 'Jessa')

if __name__ == '__main__':
    unittest.main()
