from core.models import Budget, SharedBudget, Transaction
from core.serializers import (
    BudgetSerializer,
    SharedBudgetSerializer,
    TransactionSerializer,
)
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class BudgetListView(ListCreateAPIView):
    serializer_class = BudgetSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(user=user)


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
