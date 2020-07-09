from dataclasses import dataclass

@dataclass
class Teacher:
    teacher_id: int
    f_name: str
    l_name: str
    email: str
    ssn: str
    address: str
    cid: str 