from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    MEMBERSHIP_CHOICES = (
        ('Member', 'Member'),
        ('Worker', 'Worker'),
        ('Leader', 'Leader'),
    )

    POSITION_CHOICES = (
        ('President', 'President'),
        ('Vice President', 'Vice President'),
        ('Secretary', 'Secretary'),
        ('Treasurer', 'Treasurer'),
        ('Auditor', 'Auditor'),
        ('P.R.O', 'P.R.O'),
        ('Member', 'Member'),
    )
    profile_photo = models.ImageField(upload_to='profile_photos/', default='images/profile.jpg', null=True, blank=True)
    membership_status = models.BooleanField(default=False)
    membership_type = models.CharField(max_length=50, choices=MEMBERSHIP_CHOICES, default='Member', null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, default='Member', null=True, blank=True)
    course = models.CharField(max_length=50, null=True, blank=True)
    year = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)


class LeadershipTeam(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    position = models.CharField(max_length=50, choices=CustomUser.POSITION_CHOICES, default='Member', null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    course = models.CharField(max_length=50, null=True, blank=True)
    year = models.CharField(max_length=50, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    membership_status = models.BooleanField(default=False)
    membership_type = models.CharField(max_length=50, choices=CustomUser.MEMBERSHIP_CHOICES, default='Member', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.position}"


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cover_p = models.ImageField(upload_to='event_covers/', null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    attendees = models.ManyToManyField(CustomUser, related_name='events_attending', blank=True)

    def __str__(self):
        return self.title


# create testimony model
class Testimony(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=250, default='')
    title = models.CharField(max_length=100)
    content = models.TextField()
    email = models.EmailField(default='')
    phone = models.BigIntegerField(null=True, blank=True)
    cover_p = models.ImageField(upload_to='testimony_covers/', default='images/profile.jpg', null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


# create gallery model
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    cover_p = models.ImageField(upload_to='gallery_covers/', null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


    