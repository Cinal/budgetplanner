import pytest
from core.models import Budget, BudgetUser

pytestmark = pytest.mark.django_db


@pytest.fixture
def sample_budget_user():
    return BudgetUser.objects.create(first_name="testuser", email="test@example.com")


@pytest.fixture
def sample_budget(sample_budget_user):
    return Budget.objects.create(user=sample_budget_user, name="Test Budget")


def test_budget_creation(sample_budget_user):
    budget = Budget.objects.create(user=sample_budget_user, name="Test Budget")

    assert budget.user == sample_budget_user
    assert budget.name == "Test Budget"
    assert budget.created_at is not None
