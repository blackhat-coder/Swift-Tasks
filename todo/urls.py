
from django.contrib import admin
from django.urls import path, include
from tapp import urls
from api import apiurls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
    path('api/', include(apiurls))
]