from django.urls import path
from doctor import views
urlpatterns = [

path('demo1/',views.demo,name='demo'),
path('home/',views.home,name='home'),
path('about/',views.about,name='about'),
path('services/',views.services,name='services'),
path('contact/',views.contact,name='contact'),
path('form/',views.form,name='form'),
path('adddata/',views.adddata,name='adddata'),
#path('form2/',views.form2,name='form2'),
#path('adddata2/',views.adddata2,name='adddata2'),
path('getdata/',views.getdata,name='getdata'),
path('delete/<int:id>',views.delete,name='delete'),
path('getdataforedit/<int:id>',views.getdataforedit),
path('update/<int:id>',views.update),
]
