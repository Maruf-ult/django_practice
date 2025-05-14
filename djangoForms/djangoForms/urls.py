from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('', include("first_app.urls")),  # Includes app-specific URLs
]