import random
import string

from django.db import models

class RandomGen(models.Model):
    key = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.key

    def generate_key(self):

        return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(4))

