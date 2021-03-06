from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
import json
from user.implementation.implementation import UserImplementation


# create users
class CreateStudentController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            user_implementation = UserImplementation(requests)
            payload, message = user_implementation.create_student()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


# get users
class GetStudentController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            user_implementation = UserImplementation(requests)
            payload, message = user_implementation.get_student()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class UpdateStudentController(GenericAPIView):
    def post(self,requests):
        response = {"status":200, "payload":"", "message":"", "error":""}
        try:
            requests = json.load(requests)
            student_implementation = UserImplementation(requests)
            payload, message = student_implementation.update_student()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


# delete users
class DeleteStudentController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            student_implementation = UserImplementation(requests)
            payload, message = student_implementation.delete_student()

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


# login
class LoginStudentController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            user_implementation = UserImplementation(requests)
            payload, message = user_implementation.login()

            if payload:
                response['payload'] = payload
                response['message'] = message
            else:
                response['message'] = "Invalid Credentials."
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)