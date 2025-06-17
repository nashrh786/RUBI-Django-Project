# women_empowerment/urls.py

from django.contrib import admin
from django.urls import path, include  # Import 'include' here


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # This includes URLs from the 'main' app
]
