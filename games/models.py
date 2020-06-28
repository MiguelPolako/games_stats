from django.db import models


# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '{}'.format(self.name)

    def get_detail_url(self):
        return f"/platform/{self.id}"


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)

    def get_detail_url(self):
        return f"/publisher/{self.id}"


class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def get_detail_url(self):
        return f"/genre/{self.id}"


class Game(models.Model):
    name = models.CharField(max_length=64)
    year = models.IntegerField()
    na_sales = models.IntegerField()
    eu_sales = models.IntegerField()
    jp_sales = models.IntegerField()
    platform = models.ManyToManyField(Platform)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)


    def __str__(self):
        return '{} {} {}'.format(self.name, self.year, self.platform, self.publisher, self.genres, self.na_sales,
                                 self.eu_sales, self.jp_sales)

    def get_detail_url(self):
        return f"/game/{self.id}"
