from core.models import Budget, SharedBudget, Transaction
from core.serializers import (
    BudgetSerializer,
    SharedBudgetSerializer,
    TransactionSerializer,
)
from rest_framework.generics import ListAPIView, RetrieveAPIView


class BudgetListView(ListAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class TransactionListView(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class SharedBudgetListView(ListAPIView):
    queryset = SharedBudget.objects.all()
    serializer_class = SharedBudgetSerializer


class BudgetDetailView(RetrieveAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    lookup_field = "pk"


class TransactionDetailView(RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "pk"


class SharedBudgetDetailView(RetrieveAPIView):
    queryset = SharedBudget.objects.all()
    serializer_class = SharedBudgetSerializer
    lookup_field = "pk"
