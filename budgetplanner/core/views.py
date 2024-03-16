from core.models import Budget, SharedBudget, Transaction
from core.serializers import (
    BudgetSerializer,
    SharedBudgetSerializer,
    TransactionSerializer,
)
from django.db.models import Q
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import BudgetUser


class BudgetListView(ListCreateAPIView):
    serializer_class = BudgetSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        budgets = Budget.objects.filter(user=user)
        shared_budgets_ids = SharedBudget.objects.filter(user=user).values_list("budget", flat=True)
        shared_budgets = Budget.objects.filter(id__in=shared_budgets_ids)

        return budgets | shared_budgets


class TransactionListView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = Transaction.objects.all()
        budget_id = self.request.query_params.get("budget_id", None)
        if budget_id is not None:
            queryset = queryset.filter(budget__id=budget_id)
        return queryset


class SharedBudgetListView(ListCreateAPIView):
    queryset = SharedBudget.objects.all()
    serializer_class = SharedBudgetSerializer
    pagination_class = LimitOffsetPagination


class BudgetDetailView(RetrieveAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    lookup_field = "pk"
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(Q(user=user) | Q(sharedbudget__user=user)).distinct()


class TransactionDetailView(RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "pk"


class SharedBudgetDetailView(RetrieveAPIView):
    queryset = SharedBudget.objects.all()
    serializer_class = SharedBudgetSerializer
    lookup_field = "pk"


class ShareBudgetView(APIView):
    def post(self, request, budget_id):
        email = request.data.get("email")
        if not email:
            return Response(
                {"error": "Email address is required."}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            user_to_share_with = BudgetUser.objects.get(email=email)
        except BudgetUser.DoesNotExist:
            return Response(
                {"error": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            budget = Budget.objects.get(id=budget_id)
            if SharedBudget.objects.filter(budget=budget, user=user_to_share_with).exists():
                return Response(
                    {"error": "Budget already shared with this user."},
                    status=status.HTTP_409_CONFLICT,
                )

            SharedBudget.objects.create(budget=budget, user=user_to_share_with)

            return Response({"message": "Budget shared successfully."}, status=status.HTTP_200_OK)
        except Budget.DoesNotExist:
            return Response({"error": "Budget not found."}, status=status.HTTP_404_NOT_FOUND)
