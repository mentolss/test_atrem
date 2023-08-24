from django.urls import path
from . import views
from .admin import admin_site


urlpatterns = [
    path('', views.feedback_page, name='feedback_page'),
    path('admin/', admin_site.urls),
]
