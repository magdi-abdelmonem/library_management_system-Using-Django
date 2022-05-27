from django.urls import path
from . import views 

urlpatterns = [
    
    path ('books',views.books,name='books'),
    path ('',views.index,name='index'),
    path ('update/<int:id>',views.update,name='update'),
    path ('delete/<int:id>',views.delete,name='delete'),
    
]