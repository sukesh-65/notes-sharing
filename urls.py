from django.urls import path
from hr import views
urlpatterns = [
    path('hrdash/',views.hrHome,name='hrdash'),
    
]
