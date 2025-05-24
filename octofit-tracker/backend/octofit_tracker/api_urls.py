from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('teams/', views.TeamViewSet.as_view({'get': 'list'}), name='team-list'),
    path('activities/', views.ActivityViewSet.as_view({'get': 'list'}), name='activity-list'),
    path('leaderboard/', views.LeaderboardViewSet.as_view({'get': 'list'}), name='leaderboard-list'),
    path('workouts/', views.WorkoutViewSet.as_view({'get': 'list'}), name='workout-list'),
]
