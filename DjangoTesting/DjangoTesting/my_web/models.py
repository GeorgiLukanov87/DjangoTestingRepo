from django.db import models


class Student(models.Model):
    name = models.CharField(
        max_length=30,
    )

    age = models.PositiveIntegerField()

    email = models.EmailField(
        unique=True,
    )


class Professor(models.Model):
    BASIC_LEVEL = 'Basic level'
    MID_LEVEL = 'Mid level'
    EXPERT_LEVEL = 'Expert level'

    PROFESSION_CHOICES = (
        (BASIC_LEVEL, BASIC_LEVEL),
        (MID_LEVEL, MID_LEVEL),
        (EXPERT_LEVEL, EXPERT_LEVEL),
    )

    name = models.CharField(
        max_length=30,
    )

    age = models.PositiveIntegerField()

    level = models.CharField(
        max_length=30,
        choices=PROFESSION_CHOICES,

    )


class Animal(models.Model):
    name = models.CharField(
        max_length=30,
    )

    picture_url = models.URLField()
