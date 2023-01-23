from django.urls import path
from workouts import views as workouts_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', workouts_views.index, name='home'),
    path('', workouts_views.index.as_view(), name='home'),
    path('api/workouts/', workouts_views.workout_list),
    path('api/workouts/<int:pk>/', workouts_views.workout_detail),
    # path('api/workouts/published/', workouts_views.workout_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)