from django.urls import path,include
from subject.controller.controller import (CreateSubjectController,
                                           UpdateSubjectController,
                                           DeleteSubjectController,
                                           GetSubjectController)

urlpatterns =[
    path('create/', CreateSubjectController.as_view()),
    path('get/', GetSubjectController.as_view()),
    path('update/', UpdateSubjectController.as_view()),
    path('delete/', DeleteSubjectController.as_view()),
]