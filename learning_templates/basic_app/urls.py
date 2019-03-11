from django.urls import path
from basic_app import views 

# TEMPLATE TAGGING - DJANGO IS AUTOMATICALLY GOING TO LOOK FOR APP_NAME
app_name = 'basic_app'

urlpatterns = [
	path('relative/',views.relative,name='relative'),
	path('others/',views.other,name='other')
]