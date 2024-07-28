from django.test import TestCase

class Concert(models.Model):
    concert_name = models.CharField(max_length=255)
    duration = models.IntegerField()
    city = models.CharField(max_length=255)
    date = models.DateField(default=datetime.now)

class Photo(models.Model):
    id = models.IntegerField(primary_key=True)
    pic_url = models.CharField(max_length=1000)
    event_country = models.CharField(max_length=255)
    event_state = models.CharField(max_length=255)
    event_city = models.CharField(max_length=255)
    event_date = models.DateField(default=datetime.now)

class Song(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    lyrics = models.TextField()