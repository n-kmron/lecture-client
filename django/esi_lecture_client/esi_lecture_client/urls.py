from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('book_rating.urls')),
    path('admin/', admin.site.urls),
    path('connect/', include('odoo_config.urls'))
]