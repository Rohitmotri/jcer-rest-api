from subject.models import Subject
from restapi.connection import DBConnection
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import uuid
from passlib.hash import pbkdf2_sha256
from subject.utils import get_subject_payload,subject_columns


class SubjectImplementation:
    def __init__(self, requests):
        self.requests = requests

    # create users
    def create_subject(self):
        payload = []
        count = 0
        try:
            subjects_to_create = self.requests.get("subjects", None)
            with DBConnection() as session:
                for subject in subjects_to_create:
                    _id = str(uuid.uuid4())
                    try:
                        new_user = Subject(
                            subject_id=_id,
                            subject_name=subject['subject_name'],
                            subject_code=subject['subject_code'].lower(),
                            sem=subject['sem'],
                            year=subject['year'],
                            branch_id=subject['branch_id'],
                            created_by=_id,
                            created_on=datetime.now(),
                            modified_by=_id,
                            modified_on=datetime.now(),
                        )
                        session.add(new_user)
                        session.commit()
                        payload.append({"subject_id": _id, "message": "Subject added successfully."})
                        count += 1
                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"subject_id": _id, "message": str(e._message).split(":  ")[1].split("\\")[0]})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        finally:
            return payload, str(count) + " subjects created."

    # get users
    def get_subject(self):
        payload = []
        count = 0
        message = ""
        try:
            subject_to_find = self.requests.get("subjects", None)
            with DBConnection() as session:
                if len(subject_to_find):
                    for subject in subject_to_find:
                        query = session.query(Subject).filter(Subject.subject_id == subject)
                        data = query.all()
                        if data:
                            payload1, message, count = get_subject_payload(data, count)
                            payload.append(payload1[0])
                        else:
                            payload.append({"subject_id": subject, "message": "Subject doesn't exists."})
                else:
                    query = session.query(Subject)
                    data = query.all()
                    payload, message, count = get_subject_payload(data, count)
        except Exception as e:
            print(e)
            raise e
        return payload, message

    def update_subject(self):
        payload =[]
        count = 0
        try:
            subject_to_update = self.requests.get("subject", None)
            with DBConnection() as session:
                for subject in subject_to_update:
                    columns_to_update = {}
                    for key,value in subject["update_data"].items():
                        columns_to_update[subject_columns[key]] = value
                        columns_to_update[Subject.modified_by] = subject['subject_id']
                        columns_to_update[Subject.modified_on] = datetime.now()
                    try:
                        query = session.query(Subject).filter(Subject.subject_id == subject['subject_id']) \
                            .update(columns_to_update, synchronize_session=False)
                        session.commit()
                        if query:
                            count += 1
                            payload.append({"subject_id": subject['subject_id'], "message": "Updated successfully."})
                        else:
                            payload.append({"subject_id": subject['subject_id'], "message": "Subject doesn't exist."})

                    except SQLAlchemyError as e:
                        print(e)
                        payload.append(
                            {"subject_id": subject['subject_id'], "message": str(e._message).split("Key (")[1].split(")")[0]
                                                                    + " already exists."})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " subject updated."

    # delete users
    def delete_subject(self):
        payload = []
        count = 0
        try:
            subject_to_delete = self.requests.get("subjects", None)
            with DBConnection() as session:
                for subject in subject_to_delete:
                    query = session.query(Subject).filter(Subject.subject_id == subject).delete(synchronize_session=False)
                    if query:
                        count += 1
                        payload.append({"subject_id": subject, "message": "Deleted successfully."})
                        session.commit()
                    else:
                        payload.append({"subject_id": subject, "message": "Subject doesn't exists."})
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " rows deleted."
