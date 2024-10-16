from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),  # Raiz do projeto
    path('airplane/', views.airplane, name='airplane'),
    path('airplane/details/<int:id>', views.details, name='details'),
]
