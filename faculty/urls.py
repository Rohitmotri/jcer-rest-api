from django.urls import path
from faculty.controller.controller import (CreateAdminController,
                                           GetAdminController,
                                           UpdateAdminController,
                                           DeleteAdminController)

urlpatterns = [
    path('create/', CreateAdminController.as_view()),
    path('get/', GetAdminController.as_view()),
    path('update/', UpdateAdminController.as_view()),
    path('delete/', DeleteAdminController.as_view()),

]
