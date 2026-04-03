from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)

    played = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    goal_difference = models.IntegerField(default=0)

    def points(self):
        return (self.win * 3) + self.draw

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)   # 👈 add default
    contact = models.CharField(max_length=15, blank=True) 
    email = models.EmailField(unique=True, null=True, blank=True) # 👈 allow empty
    image = models.ImageField(upload_to='managers/', blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.name