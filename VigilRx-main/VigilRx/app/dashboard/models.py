from django.db import models
from app.users.models import CustomUser  # Assuming the user model is located in users/models.py

class Transaction(models.Model):
    transaction_hash = models.CharField(max_length=255, unique=True)
    gas_usage = models.IntegerField()
    block_number = models.IntegerField()
    block_time = models.DateTimeField()
    related_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.transaction_hash

    class Meta:
        app_label = 'dashboard'
  


