from django.db import models

# Create your models here.

class Data(models.Model):
    id=models.IntegerField(primary_key=True)
    word=models.CharField(max_length=10)
    des_word=models.CharField(max_length=40)

    # def __str__(self):
    #     return self.id


class Info(models.Model):
    word=models.CharField(max_length=10)
    des_word=models.CharField(max_length=40)

    def __str__(self):
        return self.word