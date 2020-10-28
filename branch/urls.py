from django.urls import path

from branch.controller.controller import CreateBranchController, GetBranchController, DeleteBranchController,\
    UpdateBranchController

urlpatterns = [
    path('create/', CreateBranchController.as_view()),
    path('get/', GetBranchController.as_view()),
    path('delete/', DeleteBranchController.as_view()),
    path('update/', UpdateBranchController.as_view())
]