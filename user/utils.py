from user.models import Student
# from branch.models import Branches
from restapi.connection import DBConnection


# login payload
def login_payload(data):
    try:
        payload = []
        for student in data:
            new_user = {
                "student": student.user_id
            }
        payload.append(new_user)
    except Exception as e:
        print(e)
        raise e
    return payload, "Logged in successfully."


# get user payload
def get_student_payload(data, count):
    payload = []
    try:
        for student in data:
            # with DBConnection() as session:
            #     # try:
            #     #     query = session.query(Branches).filter(Branches.branch_id == user.branch_id)
            #     #     data1 = query.all()
            #     #     if data1:
            #     #         for branch in data1:
            #     #             branch_name = branch.branch_name
            #     # except Exception as e:
            #     #     print(e)
            #     #     raise e
            branch_name = 'CSE'
            new_user = {
                    "student_id": student.student_id,
                    "name": student.name,
                    "usn": student.usn,
                    "email": student.email,
                    "branch": branch_name,
                    "sem": student.sem,
                    "year": student.year,
                }
            payload.append(new_user)
            count += 1
    except Exception as e:
        print(e)
        raise e
    return payload, str(count) + " student fetched.", count


# column to update
student_columns = {
    "name": Student.name,
    "usn": Student.usn,
    "email": Student.email,
    "password": Student.password,
    "sem": Student.sem,
    "year": Student.year,
    "branch_id": Student.branch_id
}