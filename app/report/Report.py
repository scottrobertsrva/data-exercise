import json

class Report:
    def __init__(self, teacher_service, student_service, file_out):
        self.teacher_service = teacher_service
        self.student_service = student_service
        self.file_out = file_out

    def write_report(self):
        with open(self.file_out.resolve(), 'w+') as f:
            f.write("[\n")
            first_record = True
            for student in self.student_service.get_students():
                if not first_record:
                    f.write(',\n')
                first_record = False
                teacher = self.teacher_service.get_teacher(student.cid)
                student.teacher_f_name = teacher.f_name
                student.teacher_l_name = teacher.l_name
                f.write(json.dumps(student.to_dict(), indent=1))
            f.write("\n]")