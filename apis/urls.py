from django.urls import path, include

app_name = 'apis'
urlpatterns = [
    path('app/', include('apis.app.urls')),
    path('chat/', include('apis.chat.urls')),
]