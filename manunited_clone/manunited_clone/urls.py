

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from news.views import home, detail


    


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home_url'),
    path('article/<int:pk>/', detail, name='detail_url'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

