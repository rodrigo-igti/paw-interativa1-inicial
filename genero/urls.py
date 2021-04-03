from django.urls import path

from . import views

urlpatterns = [
    path('',views.cadastro,name='cadastro'),
    path('delete/<id>',views.delete,name='delete'),
    path('update/<id>',views.update,name='update'),
]