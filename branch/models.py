from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Branches(Base):
    __tablename__ = 'branch'

    branch_id = Column(String, primary_key=True)
    branch_name = Column(String)

    def __init__(self, branch_id, branch_name):
        self.branch_id = branch_id
        self.branch_name = branch_name