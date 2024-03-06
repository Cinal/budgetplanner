from django.contrib.auth.models import User
from django.db import models

from budgetplanner.core.constants import CategoryChoices, CurrencyChoices


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CategoryChoices.choices())
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CurrencyChoices.choices())
    description = models.TextField(null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.amount}"


class SharedBudget(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.budget} shared with {self.user}"
