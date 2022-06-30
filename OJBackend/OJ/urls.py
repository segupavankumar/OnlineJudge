from django .urls import path
from . import views


urlpatterns = [
    path('login',views.loginUser,name = 'login'),
    path('register',views.register,name = 'register'),
    path('logout',views.logoutUser,name = 'logout'),
    path('',views.home,name = 'home'),
    path('problem/<int:id>',views.problem_view,name = 'problem_view'),
]