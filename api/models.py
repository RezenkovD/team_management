from django.db import models

# Create your models here.


class Team(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Membership(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person} is a member of {self.team}"
