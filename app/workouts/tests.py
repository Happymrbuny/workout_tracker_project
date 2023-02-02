from django.test import TestCase
from django.urls import reverse
import pytest
from workouts.models import Workout

# Create your tests here.
def test_homepage_access():
    url = reverse('home')
    assert url == "/"

@pytest.fixture
def new_workout(db):
    workout = Workout.objects.create(
        title='Pytest',
        reps='1',
        weight='1',
        timestamp='2000-01-01',
        musclegroup='muscle'
    )
    return workout

def test_search_workouts(new_workout):
    assert Workout.objects.filter(title='Pytest').exists()

def test_update_workout(new_workout):
    new_workout.title = 'Pytest-Django'
    new_workout.save()
    assert Workout.objects.filter(title='Pytest-Django').exists()

@pytest.fixture
def another_workout(db):
    workout = Workout.objects.create(
        title='More-Pytest',
        reps='1',
        weight='1',
        timestamp='2000-01-01',
        musclegroup='muscle'
    )
    return workout

def test_compare_workouts(new_workout, another_workout):
    assert new_workout.pk != another_workout.pk