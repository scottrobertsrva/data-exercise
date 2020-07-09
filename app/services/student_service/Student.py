from dataclasses import dataclass, asdict

@dataclass
class Student:
    student_id: int
    f_name: str
    l_name: str
    email: str
    ssn: str
    address: str
    cid: str  
    teacher_f_name: str = None
    teacher_l_name: str = None  

    def to_dict(self):
        return asdict(self)