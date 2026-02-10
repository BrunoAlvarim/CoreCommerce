from django.db import models
from uuid import uuid4

class ModelCustomer (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=20,null=True)
    birth_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    hash_id = models.UUIDField(default=uuid4)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.city}"
    class Meta:
        db_table = "api.customer"