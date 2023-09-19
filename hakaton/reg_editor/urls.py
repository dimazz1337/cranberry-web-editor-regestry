from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('panel_re_editor', views.panel_re_editor, name='panel_re_editor'),
    path('add_button_click/', views.add_button_click, name='add_button_click'),
    path('save_button_click/', views.save_button_click, name='save_button_click'),
    path('del_button_click/', views.del_button_click, name='del_button_click'),
    path('search_button_click/', views.search_button_click, name='search_button_click'),
    path('profile', views.profile, name='profile'),
    path('add_user', views.add_user, name='add_user'),
    path('edit_user', views.edit_user, name='edit_user'),

]
