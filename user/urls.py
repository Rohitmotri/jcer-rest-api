from django.urls import path

from user.controller.controller import (CreateStudentController,
                                        GetStudentController,
                                        UpdateStudentController,
                                        DeleteStudentController,
                                        LoginStudentController)
urlpatterns = [
    path('create/student/', CreateStudentController.as_view()),
    path('get/student/', GetStudentController.as_view()),
    path('update/student/',UpdateStudentController.as_view()),
    path('login/student/', LoginStudentController.as_view()),
    path('delete/student/', DeleteStudentController.as_view()),
]