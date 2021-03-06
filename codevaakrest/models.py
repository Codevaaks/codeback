from django.db import models
from django.conf import settings

# Migrate this out into its own folder after we have more than 5 models or so.
# 12-31-2020 wongcoder

class Scenario(models.Model):
  scenario_name = models.CharField(max_length=100)

class Score(models.Model):
  scenario = models.ForeignKey(
    Scenario, 
    on_delete=models.CASCADE
  )

  user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE
  )

  score = models.DecimalField(max_digits=10, decimal_places=2)

