from django.db import models
from django.contrib.postgres.fields import JSONField

SOURCE_CHOICES = [
	(0, "WEB"), 
	(1, "GAME")
]

class Document(models.Model):
    owner = models.ForeignKey('auth.User', related_name='exports', null=True, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100)
    source_type = models.CharField(choices=SOURCE_CHOICES, max_length=20, blank=True)
    source_id = models.CharField(max_length=50, blank=True, null=True)
    input_meta_data = JSONField(default=dict, null=True)