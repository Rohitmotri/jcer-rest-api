from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Admin(Base):
    __tablename__ = 'admin'

    admin_id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    branch_id = Column(String)
    created_by = Column(String)
    created_on = Column(DateTime)
    modified_by = Column(String)
    modified_on = Column(DateTime)

    def __init__(self, admin_id, name,email, password, branch_id,
                 created_by, created_on, modified_by, modified_on):
        self.admin_id = admin_id
        self.name = name
        self.email = email
        self.password = password
        self.branch_id = branch_id
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on

from django.db import models

# Create your models here.
