
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from blogApp.views import index, detail
# from exercise.blogApp.views import detail
urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogApp/", index),
    path("", index),
    path("<str:pk>/", detail)
]
