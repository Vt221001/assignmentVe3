from django.contrib import admin
from django.urls import path, include  # Add this import for path and include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', lambda request: redirect('upload_csv')),  # Redirect root to the upload page
    path('admin/', admin.site.urls),
    path('upload/', include('csvdata.urls')),  # This will include URLs from the csvdata app
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
