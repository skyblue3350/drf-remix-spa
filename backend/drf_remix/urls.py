from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path

from blog.urls import router as blog_router


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/', include(blog_router.urls)),
]
