from faculty.models import Admin


def get_admin_payload(data, count):
    payload = []
    try:
        for admin in data:
            # with DBConnection() as session:
            #     try:
            #         query = session.query(Branches).filter(Branches.branch_id == user.branch_id)
            #         data1 = query.all()
            #         if data1:
            #             for branch in data1:
            #                 branch_name = branch.branch_name
            #     except Exception as e:
            #         print(e)
            #         raise e
            branch_name = 'CSE'
            new_user = {
                "admin_id":admin.admin_id,
                "name":admin.name,
                "email":admin.email,
                "branch":branch_name,
            }
            payload.append(new_user)
            count +=1
    except Exception as e:
        print(e)
        raise e
    return payload , str(count) + " admins fetched." , count


# column to update
admin_columns = {
    "name": Admin.name,
    "email": Admin.email,
    "password": Admin.password,
    "branch_id": Admin.branch_id
}