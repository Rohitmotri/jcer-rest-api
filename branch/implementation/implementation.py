from branch.models import Branches
from restapi.connection import DBConnection
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import uuid

from branch.utils import get_branches_payload


class BranchImplementation:
    def __init__(self, requests):
        self.requests = requests

    # create branches
    def create_branches(self):
        payload = []
        count = 0
        try:
            branches_to_create = self.requests.get("branches", None)
            with DBConnection() as session:
                for branch in branches_to_create:
                    _id = str(uuid.uuid4())
                    try:
                        new_branch = Branches(
                            branch_id=_id,
                            branch_name=branch['branch_name']
                        )
                        session.add(new_branch)
                        session.commit()
                        payload.append({"branch_id": _id, "message": "Branch added successfully."})
                        count += 1
                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"branch_id": _id, "message": str(e._message).split(":  ")[1].split("\\")[0]})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        finally:
            return payload, str(count) + " branches created."

    # get branches
    def get_branches(self):
        payload = []
        count = 0
        try:
            branches_to_find = self.requests.get("branches", None)
            with DBConnection() as session:
                if len(branches_to_find):
                    for branch in branches_to_find:
                        query = session.query(Branches).filter(Branches.branch_id == branch)
                        data = query.all()
                        if data:
                            payload1, message, count = get_branches_payload(data, count)
                            payload.append(payload1[0])
                        else:
                            payload.append({"branch_id": branch, "message": "Branch doesn't exists."})
                    message = str(count) + " branch fetched."
                else:
                    query = session.query(Branches)
                    data = query.all()
                    payload, message, count = get_branches_payload(data, count)
        except Exception as e:
            print(e)
            raise e
        return payload, message

    # update branches
    def update_branches(self):
        payload = []
        count = 0
        try:
            branches_to_update = self.requests.get("branches", None)
            with DBConnection() as session:
                for branch in branches_to_update:
                    columns_to_update = {
                        Branches.branch_name: branch["update_data"]["branch_name"]
                    }
                    try:
                        query = session.query(Branches).filter(Branches.branch_id == branch['branch_id']) \
                            .update(columns_to_update, synchronize_session=False)
                        session.commit()
                        if query:
                            count += 1
                            payload.append({"branch_id": branch['branch_id'], "message": "Branch updated successfully."})
                        else:
                            payload.append({"branch_id": branch['branch_id'], "message": "Branch doesn't exist."})

                    except SQLAlchemyError as e:
                        print(e)
                        payload.append(
                            {"branch_id": branch['branch_id'], "message": str(e._message).split(":  ")[1].split("\\")[0]})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " branch updated."

    # delete branches
    def delete_branches(self):
        payload = []
        count = 0
        try:
            branches_to_delete = self.requests.get('branches', None)
            with DBConnection() as session:
                for branch in branches_to_delete:
                    query = session.query(Branches).filter(Branches.branch_id == branch) \
                        .delete(synchronize_session=False)
                    if query:
                        count += 1
                        payload.append({"branch_id": branch, "message": "Branch deleted successfully."})
                        session.commit()
                    else:
                        payload.append({"branch_id": branch, "message": "Branch doesn't exists."})
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " branch deleted."