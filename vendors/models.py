from django.db import models
from accounts.models import User

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="vendor")
    business_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name

