from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('employee',views.EmployeeViewset,basename='employee')

urlpatterns = [
    path('students/', views.studentViews),
    path('students/<int:pk>/',views.studentDetailsView),
   # path('employees/',views.Employees.as_view()),
    #path('employees/<int:pk>/',views.EmployeeDeatils.as_view()),
    path('',include(router.urls)),
    path('blogs/',views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),
    path('blogs/<int:pk>/',views.BlogDeatilsView.as_view()),
    path('comments/<int:pk>/',views.CommentDeatilsView.as_view()),
     
]