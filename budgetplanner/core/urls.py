from core.views import (
    BudgetDetailView,
    BudgetListView,
    SharedBudgetDetailView,
    SharedBudgetListView,
    TransactionDetailView,
    TransactionListView,
)
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from users.views import (
    RegisterApi,
)

urlpatterns = [
    path("register/", RegisterApi.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("budgets/", BudgetListView.as_view(), name="budget-list"),
    path("budgets/<int:pk>/", BudgetDetailView.as_view(), name="budget-detail"),
    path("transactions/", TransactionListView.as_view(), name="transaction-list"),
    path("transactions/<int:pk>/", TransactionDetailView.as_view(), name="transaction-detail"),
    path("shared-budgets/", SharedBudgetListView.as_view(), name="shared-budget-list"),
    path("shared-budgets/<int:pk>/", SharedBudgetDetailView.as_view(), name="shared-budget-detail"),
]
