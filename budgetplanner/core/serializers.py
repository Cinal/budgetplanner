from typing import Dict

from core.models import Budget, SharedBudget, Transaction
from rest_framework.serializers import ModelSerializer


class BudgetSerializer(ModelSerializer):
    class Meta:
        model = Budget
        fields = "__all__"

    def to_representation(self, instance: Budget) -> Dict:
        representation = super().to_representation(instance)

        # Add pagination information to the representation
        pagination = self.context.get("pagination")
        if pagination:
            representation["pagination"] = {
                "count": pagination.count,
                "next": pagination.get_next_link(),
                "previous": pagination.get_previous_link(),
            }
        return representation


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class SharedBudgetSerializer(ModelSerializer):
    class Meta:
        model = SharedBudget
        fields = "__all__"
