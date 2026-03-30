from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create_user(username='tony', email='tony@marvel.com', password='ironman', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@marvel.com', password='cap', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@marvel.com', password='hulk', team=marvel)
        clark = User.objects.create_user(username='clark', email='clark@dc.com', password='superman', team=dc)
        bruce_dc = User.objects.create_user(username='bruce_dc', email='bruce@dc.com', password='batman', team=dc)
        diana = User.objects.create_user(username='diana', email='diana@dc.com', password='wonderwoman', team=dc)

        # Create activities
        Activity.objects.create(user=tony, type='run', duration=30, distance=5)
        Activity.objects.create(user=steve, type='cycle', duration=60, distance=20)
        Activity.objects.create(user=clark, type='swim', duration=45, distance=2)

        # Create workouts
        Workout.objects.create(name='Morning Cardio', description='30 min run + 20 min cycle')
        Workout.objects.create(name='Strength', description='Pushups, Pullups, Squats')

        # Create leaderboard
        Leaderboard.objects.create(user=tony, points=100)
        Leaderboard.objects.create(user=clark, points=120)
        Leaderboard.objects.create(user=steve, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
