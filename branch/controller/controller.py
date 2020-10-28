from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
import json
from branch.implementation.implementation import BranchImplementation


# create branches
class CreateBranchController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            branch_implementation = BranchImplementation(requests)
            payload, message = branch_implementation.create_branches()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


# get branches
class GetBranchController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            branch_implementation = BranchImplementation(requests)
            payload, message = branch_implementation.get_branches()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


# delete branches
class DeleteBranchController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            branch_implementation = BranchImplementation(requests)
            payload, message = branch_implementation.delete_branches()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


# update branches
class UpdateBranchController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            branch_implementation = BranchImplementation(requests)
            payload, message = branch_implementation.update_branches()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)