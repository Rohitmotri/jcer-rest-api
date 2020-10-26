from faculty.models import Admin
from restapi.connection import DBConnection
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import uuid
from passlib.hash import pbkdf2_sha256
from faculty.utils import get_admin_payload,admin_columns


class AdminImplementation:
    def __init__(self, requests):
        self.requests = requests

    # create users
    def create_admin(self):
        payload = []
        count = 0
        try:
            admin_to_create = self.requests.get("admins", None)
            with DBConnection() as session:
                for admin in admin_to_create:
                    _id = str(uuid.uuid4())
                    try:
                        new_user = Admin(
                            admin_id=_id,
                            name=admin['name'],
                            email=admin['email'],
                            password=pbkdf2_sha256.encrypt(admin['password'], rounds=1200, salt_size=32),
                            branch_id=admin['branch_id'],
                            created_by=_id,
                            created_on=datetime.now(),
                            modified_by=_id,
                            modified_on=datetime.now(),
                        )
                        session.add(new_user)
                        session.commit()
                        payload.append({"admin_id": _id, "message": "Admin added successfully."})
                        count += 1
                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"admin_id": _id, "message": str(e._message).split(":  ")[1].split("\\")[0]})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        finally:
            return payload, str(count) + " admins created."

    def get_admin(self):
        payload = []
        count= 0
        message = ""
        try:
            admin_to_get = self.requests.get("admins", None)
            with DBConnection() as session:
                if len(admin_to_get):
                    for admin in admin_to_get:
                        query = session.query(Admin).filter(Admin.admin_id == admin)
                        data = query.all()
                        if data:
                            payload1,message,count = get_admin_payload(data,count)
                            payload.append(payload1[0])
                        else:
                            payload.append({"admin_id": admin, "message": "Admin doesn't exists."})
                else:
                    query = session.query(Admin)
                    data = query.all()
                    payload,message,count = get_admin_payload(data, count)
        except Exception as e:
            print(e)
            raise e
        return payload,message

    def update_admin(self):
        payload = []
        count = 0
        try:
            admin_to_update = self.requests.get("admins", None)
            with DBConnection() as session:
                for admin in admin_to_update:
                    columns_to_update = {}
                    for key, value in admin["update_data"].items():
                        if key == "password":
                            value = pbkdf2_sha256.encrypt(value, rounds=1200, salt_size=32)
                            columns_to_update[admin_columns[key]] = value
                        columns_to_update[admin_columns[key]] = value
                        columns_to_update[Admin.modified_by] = admin['admin_id']
                        columns_to_update[Admin.modified_on] = datetime.now()
                    try:

                        query = session.query(Admin).filter(Admin.admin_id == admin['admin_id']) \
                            .update(columns_to_update, synchronize_session=False)
                        session.commit()
                        if query:
                            count += 1
                            payload.append({"admin_id": admin['admin_id'], "message": "Updated successfully."})
                        else:
                            payload.append({"admin_id": admin['admin_id'], "message": "Faculty doesn't exist."})

                    except SQLAlchemyError as e:
                        print(e)
                        payload.append(
                            {"admin_id": admin['admin_id'], "message": str(e._message)})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " Faculty updated."

    # delete users
    def delete_admin(self):
        payload = []
        count = 0
        try:
            admin_to_delete = self.requests.get("admins", None)
            with DBConnection() as session:
                for admin in admin_to_delete:
                    query = session.query(Admin).filter(Admin.admin_id == admin).delete(
                        synchronize_session=False)
                    if query:
                        count += 1
                        payload.append({"admin_id": admin, "message": "Deleted successfully."})
                        session.commit()
                    else:
                        payload.append({"admin_id": admin, "message": "Admin doesn't exists."})
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " admin deleted."

    # login
    def login(self):
        payload = []
        message = ""
        try:
            admin = self.requests.get("admin", None)
            with DBConnection() as session:
                try:
                    query = session.query(Admin.student_id, Admin.email, Admin.password).filter(
                        Admin.email == Admin[0]["email"].lower())
                    data = query.all()
                    if data:
                        if pbkdf2_sha256.verify(Admin[0]["password"], data[0][2]):
                            payload.append({"admin_id": data[0][0]})
                            message = "sucessfully login"
                except Exception as e:
                    print(e)
                    raise e
        except Exception as e:
            print(e)
            raise e
        return payload, message


