from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
import json
from subject.implementation.implementation import SubjectImplementation


# create users
class CreateSubjectController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            subject_implementation = SubjectImplementation(requests)
            payload, message = subject_implementation.create_subject()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


# get users
class GetSubjectController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            subject_implementation = SubjectImplementation(requests)
            payload, message = subject_implementation.get_subject()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class UpdateSubjectController(GenericAPIView):
    def post(self,requests):
        response = {"status":200, "payload":"", "message":"", "error":""}
        try:
            requests = json.load(requests)
            subject_implementation = SubjectImplementation(requests)
            payload, message = subject_implementation.update_subject()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


# delete users
class DeleteSubjectController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            subject_implementation = SubjectImplementation(requests)
            payload, message = subject_implementation.delete_subject()

            if payload:
                response['payload'] = payload
                response['message'] = message
            else:
                response['message'] = "student id required. "
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)
