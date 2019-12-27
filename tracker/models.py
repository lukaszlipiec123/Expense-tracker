from django.db import models
from django.contrib.auth.models import User

class MoneyChange(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    isIncome = models.BooleanField()
    value = models.IntegerField()
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
