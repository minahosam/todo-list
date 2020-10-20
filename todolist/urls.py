from django.urls import include, path
from . import views
app_name='todolist'
urlpatterns = [
    ### class based views
    path('cbv/',views.showlist.as_view(),name='list'),
    path('cbv/',views.newtodo.as_view(),name='new'),
    path('cbv/<pk>/update/',views.update1.as_view(),name='update1'),
    ### function based view
    path('',views.new,name='add'),
    path('<id>/update/',views.update,name='update'),
    path('<id>/delete/',views.delete,name='delete'),
]
