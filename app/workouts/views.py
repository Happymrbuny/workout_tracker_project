from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from workouts.models import Workout
from workouts.serializers import WorkoutSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "workouts/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Workout.objects.all()
    return render(request, "workouts/index.html", {'workouts': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'workouts/index.html'

    def get(self, request):
        queryset = Workout.objects.all()
        return Response({'workouts': queryset})


class list_all_workouts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'workouts/workout_list.html'

    def get(self, request):
        queryset = Workout.objects.all()
        return Response({'workouts': queryset})


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def workout_list(request):
    if request.method == 'GET':
        workouts = Workout.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            workouts = workouts.filter(title__icontains=title)

        workouts_serializer = WorkoutSerializer(workouts, many=True)
        return JsonResponse(workouts_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        workout_data = JSONParser().parse(request)
        workout_serializer = WorkoutSerializer(data=workout_data)
        if workout_serializer.is_valid():
            workout_serializer.save()
            return JsonResponse(workout_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(workout_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Workout.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Workouts were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def workout_detail(request, pk):
    try:
        workout = Workout.objects.get(pk=pk)
    except Workout.DoesNotExist:
        return JsonResponse({'message': 'The workout does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        workout_serializer = WorkoutSerializer(workout)
        return JsonResponse(workout_serializer.data)

    elif request.method == 'PUT':
        workout_data = JSONParser().parse(request)
        workout_serializer = WorkoutSerializer(workout, data=workout_data)
        if workout_serializer.is_valid():
            workout_serializer.save()
            return JsonResponse(workout_serializer.data)
        return JsonResponse(workout_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        workout.delete()
        return JsonResponse({'message': 'Workout was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def workout_list_published(request):
    workouts = Workout.objects.filter(published=True)

    if request.method == 'GET':
        workouts_serializer = WorkoutSerializer(workouts, many=True)
        return JsonResponse(workouts_serializer.data, safe=False)