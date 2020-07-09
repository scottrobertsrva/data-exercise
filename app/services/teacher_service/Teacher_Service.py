from pyarrow import parquet as pq
import pandas as pd
from .Teacher import Teacher

class Teacher_Service:
    def __init__(self, data_file):
        self.data_file = data_file

    def get_teacher(self, cid):
        parquet_file = pq.ParquetFile(self.data_file)
        read_group = parquet_file.num_row_groups - 1
        teacher = None
        while read_group >= 0:
            df = parquet_file.read_row_group(read_group).to_pandas()
            df = df[df['cid']==cid]
            if df['id'].count() == 1:
                row = df.iloc[0]
                teacher = Teacher(teacher_id = row['id'], f_name = row['fname'], 
                                          l_name = row['lname'], email = row['email'],
                                          ssn = row['ssn'], address = row['address'],
                                          cid = row['cid'])
                break
            read_group = read_group - 1
        return teacher
