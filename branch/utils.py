# get branches payload
def get_branches_payload(data, count):
    try:
        payload = []
        for branch in data:
            new_branch = {
                "branch_id": branch.branch_id,
                "branch_name": branch.branch_name
            }
            payload.append(new_branch)
            count += 1
    except Exception as e:
        print(e)
        raise e
    return payload, str(count) + " branches fetched.", count