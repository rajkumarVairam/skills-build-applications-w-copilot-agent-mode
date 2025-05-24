from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    class Meta:
        abstract = False

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ArrayField(model_container=User)
    class Meta:
        abstract = False

class Activity(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    class Meta:
        abstract = False

class Leaderboard(models.Model):
    team = models.EmbeddedField(model_container=Team)
    score = models.IntegerField()
    class Meta:
        abstract = False

class Workout(models.Model):
    user = models.EmbeddedField(model_container=User)
    activity = models.EmbeddedField(model_container=Activity)
    date = models.DateField()
    class Meta:
        abstract = False