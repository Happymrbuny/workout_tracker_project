from django.urls import path
from workouts import views as workouts_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', workouts_views.index.as_view(), name='home'),
    path('api/workouts/', workouts_views.workout_list, name='workouts-list'),
    path('api/workouts/<int:pk>/', workouts_views.workout_detail, name='worout-detail'),
    path('api/workouts/date/<str:timestamp>/', workouts_views.workout_date, name='workout-date'),
    path('api/workouts/title/<str:title>/', workouts_views.workout_title, name='workout-title'),
    path('api/workouts/group/<str:musclegroup>/', workouts_views.workout_group, name='workout-group'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)