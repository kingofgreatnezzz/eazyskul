from django.urls import path 
from . import views

app_name = 'halls'

urlpatterns = [
    path('', views.hall_list, name="hall_list"),
    path("clearance/", views.clearance, name="clearance"),
    path("howto/", views.howto, name='howto'),
    path('reg_page/',views.reg_page ,name='reg_page'),
    path("kga/", views.kga, name='kga'),
    path('<slug:hall_slug>/', views.hall_list, name="hall_list_by_category"),
    path('<int:id>/<slug:slug>/', views.hall_detail, name="hall_detail"), 
]