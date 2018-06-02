from django.urls import path
from . import views

urlpatterns=[
    path("index/", views.index),
    path("home/", views.home),
    path("yingYi/", views.yingYi),
    path("yingEr/", views.yingEr),
    path("course/", views.course),
    path("information/", views.information),
    path("comprehension1/<int:moduleid>/", views.comprehension1),
    # path("comprehension2/", views.comprehension2),
    # path("clozeText1/", views.clozeText1),
    # path("clozeText2/", views.clozeText2),
    # path("writing1/", views.writing1),
    # path("writing2/", views.writing2),
    # path("translation1/", views.translation1),
    # path("translation2/", views.translation2),
    path("courseList11/<int:engmoduid>/", views.courseList11),
    # path("courseList12/", views.courseList12),
    # path("courseList13/", views.courseList13),
    # path("courseList14/", views.courseList14),
    # path("courseList21/", views.courseList21),
    # path("courseList22/", views.courseList22),
    # path("courseList23/", views.courseList23),
    # path("courseList24/", views.courseList24),
    path("register/", views.register),
    path("alert/", views.alert),

    path('login_handle/', views.login_handle),#登录处理
    path('register_handle/', views.register_handle), #注册处理
    path('buy_handle/', views.buy_handle),   #购买处理
    path('modify_handle/', views.modify_handle),   #修改处理

]
app_name = 'qingye'
