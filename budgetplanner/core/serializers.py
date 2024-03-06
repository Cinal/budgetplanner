from rest_framework.serializers import (
    ModelSerializer,
)

from budgetplanner.core.models import Budget, SharedBudget, Transaction


class BudgetSerializer(ModelSerializer):
    class Meta:
        model = Budget
        fields = "__all__"


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class SharedBudgetSerializer(ModelSerializer):
    class Meta:
        model = SharedBudget
        fields = "__all__"
