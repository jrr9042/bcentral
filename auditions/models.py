from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class Audition(models.Model):
    company = models.ForeignKey(Company)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=5)
    address = models.CharField(max_length=255)
    time = models.DateTimeField()
    url = models.URLField('info_url', null=True)

    def __str__(self):
        city_state = "{0} : {1}, {2}"
        return city_state.format(self.company, self.city, self.state)
