from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('insert/', views.insert, name='insert'),
    path('insertdata/', views.insertdata, name='insertdata'),
    path('viewproducts/', views.viewproducts, name='viewproducts'),
    path('update/<id>', views.update, name='update'),
    path('delete_data/<id>', views.delete_dt, name='delete_data'),

]