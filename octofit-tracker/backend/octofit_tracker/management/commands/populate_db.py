from django.core.management.base import BaseCommand
import random
from datetime import date, timedelta
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, workouts, and leaderboard.'

    def handle(self, *args, **options):
        users = self.create_users()
        teams = self.create_teams(users)
        self.create_activities(users)
        self.create_workouts(users)
        self.create_leaderboard(teams)
        self.stdout.write(self.style.SUCCESS('Test data created successfully.'))

    def create_users(self):
        users = []
        for i in range(5):
            user, _ = User.objects.get_or_create(
                username=f'user{i}',
                email=f'user{i}@example.com',
                first_name=f'First{i}',
                last_name=f'Last{i}',
            )
            users.append(user)
        return users

    def create_teams(self, users):
        teams = []
        for i in range(2):
            team, _ = Team.objects.get_or_create(
                name=f'Team{i}',
            )
            team.members.set(users[i*2:i*2+3])
            team.save()
            teams.append(team)
        return teams

    def create_activities(self, users):
        for user in users:
            for j in range(3):
                Activity.objects.get_or_create(
                    user=user,
                    activity_type=random.choice(['run', 'walk', 'cycle']),
                    duration=random.randint(20, 120),
                    calories_burned=random.randint(100, 800),
                    date=date.today() - timedelta(days=j)
                )

    def create_workouts(self, users):
        for user in users:
            for j in range(2):
                Workout.objects.get_or_create(
                    user=user,
                    name=f'Workout{j}',
                    description=f'Description for workout {j}',
                    date=date.today() - timedelta(days=j)
                )

    def create_leaderboard(self, teams):
        for team in teams:
            Leaderboard.objects.get_or_create(
                team=team,
                total_points=random.randint(100, 1000),
                week=date.today()
            )
