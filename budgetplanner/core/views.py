from core.models import Budget, SharedBudget, Transaction
from core.serializers import (
    BudgetSerializer,
    SharedBudgetSerializer,
    TransactionSerializer,
)
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.pagination import LimitOffsetPagination


class BudgetListView(ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    pagination_class = LimitOffsetPagination


class TransactionListView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = LimitOffsetPagination


class SharedBudgetListView(ListCreateAPIView):
    queryset = SharedBudget.objects.all()
    serializer_class = SharedBudgetSerializer
    pagination_class = LimitOffsetPagination


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
