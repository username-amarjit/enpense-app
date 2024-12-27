from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    CATEGORY_CHOICES = (
        ('GROCERIES', 'Groceries'),
        ('LEISURE', 'Leisure'),
        ('ELECTRONICS', 'Electronics'),
        ('UTILITIES', 'Utilities'),
        ('CLOTHING', 'Clothing'),
        ('HEALTH', 'Health'),
        ('OTHERS', 'Others'),
    )

    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name="expense_user")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    description = models.CharField(max_length=200, blank=True)
    
# Create your models here.
