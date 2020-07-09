from report import Report
from services import Teacher_Service, Student_Service
from pathlib import Path


def get_file_paths(data_folder, student_filename, teacher_filename, output_folder, output_filename):
    root_dir = Path(__file__, '..')
    student_data = root_dir / data_folder / student_filename
    teacher_data = root_dir / data_folder / teacher_filename
    output_file = root_dir / output_folder / output_filename
    return student_data, teacher_data, output_file


def main():
    # file variables
    data_folder = 'data'
    student_filename = 'students.csv'
    teacher_filename = 'teachers.parquet'
    output_folder = 'output'
    output_filename = 'report.json'
    
    # get file paths
    student_csv_file, teacher_parquet_file, output_file = get_file_paths(data_folder, student_filename, teacher_filename, output_folder, output_filename)

    # instantiate report
    json_report = Report(Teacher_Service.Teacher_Service(teacher_parquet_file), Student_Service.Student_Service(student_csv_file), output_file)

    # write the report
    json_report.write_report()


if __name__ == "__main__":
    main()