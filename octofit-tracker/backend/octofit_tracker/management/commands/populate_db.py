from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index({'email': 1}, unique=True)

        # Sample data
        marvel_team = {'name': 'Marvel', 'members': ['Iron Man', 'Captain America', 'Thor', 'Black Widow']}
        dc_team = {'name': 'DC', 'members': ['Superman', 'Batman', 'Wonder Woman', 'Flash']}

        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'Marvel'},
            {'name': 'Thor', 'email': 'thor@marvel.com', 'team': 'Marvel'},
            {'name': 'Black Widow', 'email': 'widow@marvel.com', 'team': 'Marvel'},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': 'DC'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
            {'name': 'Flash', 'email': 'flash@dc.com', 'team': 'DC'},
        ]

        teams = [marvel_team, dc_team]

        activities = [
            {'user': 'Iron Man', 'activity': 'Running', 'duration': 30},
            {'user': 'Batman', 'activity': 'Cycling', 'duration': 45},
            {'user': 'Wonder Woman', 'activity': 'Swimming', 'duration': 60},
        ]

        leaderboard = [
            {'team': 'Marvel', 'points': 120},
            {'team': 'DC', 'points': 110},
        ]

        workouts = [
            {'name': 'Morning Cardio', 'suggested_for': ['Iron Man', 'Superman']},
            {'name': 'Strength Training', 'suggested_for': ['Thor', 'Wonder Woman']},
        ]

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
