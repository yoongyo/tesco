from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('product/', include(('product.urls', 'product'), namespace='product')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
    path('technology/', include(('develop.urls', 'develop'), namespace='develop')),
    path('introduction', include(('introduction.urls', 'introduction'), namespace='introduction'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
