from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email="user1@example.com", name="User One")
        user2 = User.objects.create(email="user2@example.com", name="User Two")

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha", members=[user1, user2])

        # Create test activities
        activity1 = Activity.objects.create(name="Running", duration=30)
        activity2 = Activity.objects.create(name="Cycling", duration=60)

        # Create test leaderboard
        leaderboard1 = Leaderboard.objects.create(team=team1, score=100)

        # Create test workouts
        Workout.objects.create(user=user1, activity=activity1, date="2025-05-24")
        Workout.objects.create(user=user2, activity=activity2, date="2025-05-24")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
