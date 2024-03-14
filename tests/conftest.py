import pytest
from core.models import Budget, BudgetUser
from pytest_factoryboy import register

from tests.factories import (
    BudgetFactory,
    BudgetUserFactory,
    SharedBudgetFactory,
    TransactionFactory,
)

pytestmark = pytest.mark.django_db


register(BudgetUserFactory)
register(BudgetFactory)
register(TransactionFactory)
register(SharedBudgetFactory)


@pytest.fixture
def sample_budget_user():
    return BudgetUser.objects.create(first_name="testuser", email="test@example.com")


@pytest.fixture
def sample_budget(sample_budget_user):
    return Budget.objects.create(user=sample_budget_user, name="Test Budget")
