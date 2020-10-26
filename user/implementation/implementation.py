from user.models import Student
from restapi.connection import DBConnection
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import uuid
from passlib.hash import pbkdf2_sha256
from user.utils import get_student_payload,student_columns,login_payload


class UserImplementation:
    def __init__(self, requests):
        self.requests = requests

    # create users
    def create_student(self):
        payload = []
        count = 0
        try:
            students_to_create = self.requests.get("students", None)
            with DBConnection() as session:
                for student in students_to_create:
                    _id = str(uuid.uuid4())
                    try:
                        new_user = Student(
                            student_id=_id,
                            name=student['name'],
                            usn=student['usn'].lower(),
                            email=student['email'],
                            password=pbkdf2_sha256.encrypt(student['password'], rounds=1200, salt_size=32),
                            sem=student['sem'],
                            year=student['year'],
                            branch_id=student['branch_id'],
                            created_by=_id,
                            created_on=datetime.now(),
                            modified_by=_id,
                            modified_on=datetime.now(),
                        )
                        session.add(new_user)
                        session.commit()
                        payload.append({"student_id": _id, "message": "Student added successfully."})
                        count += 1
                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"student_id": _id, "message": str(e._message).split(":  ")[1].split("\\")[0]})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        finally:
            return payload, str(count) + " students created."

    # get users
    def get_student(self):
        payload = []
        count = 0
        message = ""
        try:
            student_to_find = self.requests.get("students", None)
            with DBConnection() as session:
                if len(student_to_find):
                    for student in student_to_find:
                        query = session.query(Student).filter(Student.student_id == student)
                        data = query.all()
                        if data:
                            payload1, message, count = get_student_payload(data, count)
                            payload.append(payload1[0])
                        else:
                            payload.append({"student_id": student, "message": "Student doesn't exists."})
                else:
                    query = session.query(Student)
                    data = query.all()
                    payload, message, count = get_student_payload(data, count)
        except Exception as e:
            print(e)
            raise e
        return payload, message

    def update_student(self):
        payload =[]
        count = 0
        try:
            student_to_update = self.requests.get("students", None)
            with DBConnection() as session:
                for student in student_to_update:
                    columns_to_update = {}
                    for key,value in student["update_data"].items():
                        if key == "password":
                            value = pbkdf2_sha256.encrypt(value,rounds=1200,salt_size=32)
                            columns_to_update[student_columns[key]] = value
                        columns_to_update[student_columns[key]] = value
                        columns_to_update[Student.modified_by] = student['student_id']
                        columns_to_update[Student.modified_on] = datetime.now()
                    try:
                        query = session.query(Student).filter(Student.student_id == student['student_id']) \
                            .update(columns_to_update, synchronize_session=False)
                        session.commit()
                        if query:
                            count += 1
                            payload.append({"student_id": student['student_id'], "message": "Updated successfully."})
                        else:
                            payload.append({"student_id": student['student_id'], "message": "Student doesn't exist."})

                    except SQLAlchemyError as e:
                        print(e)
                        payload.append(
                            {"student_id": student['student_id'], "message": str(e._message).split("Key (")[1].split(")")[0]
                                                                    + " already exists."})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " student updated."

    # delete users
    def delete_student(self):
        payload = []
        count = 0
        try:
            student_to_delete = self.requests.get("students", None)
            with DBConnection() as session:
                for student in student_to_delete:
                    query = session.query(Student).filter(Student.student_id == student).delete(synchronize_session=False)
                    if query:
                        count += 1
                        payload.append({"student_id": student, "message": "Deleted successfully."})
                        session.commit()
                    else:
                        payload.append({"student_id": student, "message": "Student doesn't exists."})
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " rows deleted."

    # login
    def login(self):
        payload = []
        message = ""
        try:
            student = self.requests.get("student", None)
            with DBConnection() as session:
                try:
                    query = session.query(Student.student_id, Student.usn, Student.password).filter(Student.usn == student[0]["usn"].lower())
                    data = query.all()
                    if data:
                        if pbkdf2_sha256.verify(student[0]["password"], data[0][2]):
                            payload.append({"student_id": data[0][0]})
                            message = "sucessfully login"
                except Exception as e:
                    print(e)
                    raise e
        except Exception as e:
            print(e)
            raise e
        return payload, message
