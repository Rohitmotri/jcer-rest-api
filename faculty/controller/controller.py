from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
import json
from faculty.implementation.implementation import AdminImplementation


# create users
class CreateAdminController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            admin_implementation = AdminImplementation(requests)
            payload, message = admin_implementation.create_admin()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class GetAdminController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            admin_implementation = AdminImplementation(requests)
            payload, message = admin_implementation.get_admin()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class UpdateAdminController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            admin_implementation = AdminImplementation(requests)
            payload, message = admin_implementation.update_admin()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class DeleteAdminController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            admin_implementation = AdminImplementation(requests)
            payload, message = admin_implementation.delete_admin()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)