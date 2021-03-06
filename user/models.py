from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    student_id = Column(String, primary_key=True)
    name = Column(String)
    usn = Column(String)
    email = Column(String)
    password = Column(String)
    branch_id = Column(String)
    sem = Column(Integer)
    year = Column(Integer)
    created_by = Column(String)
    created_on = Column(DateTime)
    modified_by = Column(String)
    modified_on = Column(DateTime)

    def __init__(self, student_id, name, usn, password, email, sem, year, branch_id,
                 created_by, created_on, modified_by, modified_on):
        self.student_id = student_id
        self.name = name
        self.usn = usn
        self.password = password
        self.email = email
        self.sem = sem
        self.year = year
        self.branch_id = branch_id
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on

