# from django.contrib import admin
from django.urls import path
from imageuploadapp import views
# from django.conf import settings
# from django.conf.urls.static import  static

urlpatterns = [
    path('create_blog/',views.BlogCreateAPIView.as_view()),
    path('get_blogs/',views.BlogGetAPIView.as_view()),
    path('send_mail/',views.SendEmailAPIView.as_view()),
]
