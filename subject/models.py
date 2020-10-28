from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Subject(Base):
    __tablename__ = "subject"

    subject_id = Column(String, primary_key=True)
    subject_name = Column(String)
    subject_code = Column(String)
    branch_id = Column(String)
    sem = Column(Integer)
    year = Column(Integer)
    created_by = Column(String)
    created_on = Column(DateTime)
    modified_by = Column(String)
    modified_on = Column(DateTime)

    def __init__(self, subject_id, subject_name, subject_code, branch_id,sem,year,
                 created_by, created_on, modified_by, modified_on):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.subject_code = subject_code
        self.branch_id = branch_id
        self.sem = sem
        self.year = year
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on
