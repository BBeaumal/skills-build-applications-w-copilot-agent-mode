from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        user = User.objects.create_user(username='testuser', email='test@marvel.com', password='pass', team=marvel)
        Activity.objects.create(user=user, type='run', duration=30)
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', team=marvel)
        Leaderboard.objects.create(user=user, points=100)

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 1)

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard_creation(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
