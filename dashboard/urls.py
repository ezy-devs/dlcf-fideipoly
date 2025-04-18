from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_home, name='dashboard_home'),
    path('profile/', views.admin_profile, name='admin_profile'),
    path('events/all', views.events_list, name='events_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/update/<int:event_id>/', views.update_event, name='update_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    # users urls
    path('users/', views.users_list, name='users_list'),
    path('users/detail/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/update/<int:user_id>/', views.update_user, name='update_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('testimonies', views.testimonies_list, name='testimonies_list'),
    # create_testimony
    path('testimonies/create/', views.new_testimony, name='create_testimony'),
    path('testimonies/update/<int:pk>/', views.update_testimony, name='update_testimony'),  
    path('testimonies/<int:pk>/', views.testimony_detail, name='testimony_detail'),
    path('testimonies/delete/<int:pk>/', views.delete_testimony, name='delete_testimony'),
    # approve testimony
    path('testimonies/approve/<int:pk>/', views.approve_testimony, name='approve_testimony'),
    # path('members/', views.members_list, name='members_list'),
    # path('members/<int:member_id>/', views.member_detail, name='member_detail'),
    # path('members/create/', views.create_member, name='create_member'),
    # path('members/update/<int:member_id>/', views.update_member, name='update_member'),
    # path('members/delete/<int:member_id>/', views.delete_member, name='delete_member'),
    # path('team/', views.team_list, name='team_list'),
    # path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    # path('team/create/', views.create_team, name='create_team'),
    # path('team/update/<int:team_id>/', views.update_team, name='update_team'),
]