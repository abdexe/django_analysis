from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('pages.urls')),
    path('',include('contacts.urls')),
    path('accounts/',include('accounts.urls')),
    path('surveys/',include('surveys.urls')),
    path('data_analysis/',include('data_analysis.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)