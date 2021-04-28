from django.db import models
from django.utils.crypto import get_random_string

def generate_unique_code():
  while True:
    code = get_random_string(length=6)
    # if the generated code exists, stop the loop and return the code
    if Room.objects.filter(code=code).exists():
      break

  return code

# Create your models here.
class Room(models.Model):
  code = models.CharField(max_length=8, default='', unique=True)
  host = models.CharField(max_length=50, unique=True)
  guest_can_pause = models.BooleanField(null=False, default=False)
  votes_to_skip = models.IntegerField(null=False, default=1)
  created_at = models.DateTimeField(auto_now_add=True)