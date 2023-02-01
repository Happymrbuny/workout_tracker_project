from django.urls import path
from workouts import views as workouts_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', workouts_views.index.as_view(), name='home'),
    path('api/workouts/', workouts_views.workout_list),
    path('api/workouts/<int:pk>/', workouts_views.workout_detail),
    path('api/workouts/date/<str:timestamp>/', workouts_views.workout_date),
    path('api/workouts/title/<str:title>/', workouts_views.workout_title),
    path('api/workouts/group/<str:musclegroup>/', workouts_views.workout_group),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)