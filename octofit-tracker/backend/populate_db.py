import os
import django
import random
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

def create_users():
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

def create_teams(users):
    teams = []
    for i in range(2):
        team, _ = Team.objects.get_or_create(
            name=f'Team{i}',
        )
        team.members.set(users[i*2:i*2+3])
        team.save()
        teams.append(team)
    return teams

def create_activities(users):
    for user in users:
        for j in range(3):
            Activity.objects.get_or_create(
                user=user,
                activity_type=random.choice(['run', 'walk', 'cycle']),
                duration=random.randint(20, 120),
                calories_burned=random.randint(100, 800),
                date=date.today() - timedelta(days=j)
            )

def create_workouts(users):
    for user in users:
        for j in range(2):
            Workout.objects.get_or_create(
                user=user,
                name=f'Workout{j}',
                description=f'Description for workout {j}',
                date=date.today() - timedelta(days=j)
            )

def create_leaderboard(teams):
    for team in teams:
        Leaderboard.objects.get_or_create(
            team=team,
            total_points=random.randint(100, 1000),
            week=date.today()
        )

def main():
    users = create_users()
    teams = create_teams(users)
    create_activities(users)
    create_workouts(users)
    create_leaderboard(teams)
    print('Test data created successfully.')

if __name__ == '__main__':
    main()
