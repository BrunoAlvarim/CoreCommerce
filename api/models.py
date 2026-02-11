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

class ModelProduct(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    hash_id = models.UUIDField(default=uuid4)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        db_table = "api.product"

# class Sale(models.Model):
#     cpf_cliente = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     total_value = models.DecimalField(max_digits=12, decimal_places=2)
#     sale_date = models.DateTimeField()