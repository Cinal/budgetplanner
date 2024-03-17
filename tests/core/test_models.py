from datetime import date

import pytest
from core.models import Budget, SharedBudget, Transaction

pytestmark = pytest.mark.django_db


def test_budget_creation(sample_budget_user):
    budget = Budget.objects.create(user=sample_budget_user, name="Test Budget")

    assert budget.user == sample_budget_user
    assert budget.name == "Test Budget"
    assert budget.created_at is not None


def test_budget_string_representation(sample_budget_user):
    budget = Budget.objects.create(user=sample_budget_user, name="Test Budget")

    assert str(budget) == "2. Test Budget - test@example.com"


def test_transaction_creation(sample_budget):
    transaction = Transaction.objects.create(
        budget=sample_budget,
        category="Food",
        amount=100.00,
        currency="USD",
        description="Test transaction",
        date=date.today(),
    )

    assert transaction.budget == sample_budget
    assert transaction.category == "Food"
    assert transaction.amount == 100.00
    assert transaction.currency == "USD"
    assert transaction.description == "Test transaction"
    assert transaction.date == date.today()


def test_shared_budget_str(sample_budget, sample_budget_user):
    shared_budget = SharedBudget.objects.create(budget=sample_budget, user=sample_budget_user)
    assert str(shared_budget) == "4. Test Budget - test@example.com shared with test@example.com"


def test_shared_budget_creation(sample_budget_user, sample_budget):
    """Test SharedBudget creation."""
    initial_count = SharedBudget.objects.count()
    shared_budget = SharedBudget.objects.create(budget=sample_budget, user=sample_budget_user)
    assert SharedBudget.objects.count() == initial_count + 1
    assert shared_budget.budget == sample_budget
    assert shared_budget.user == sample_budget_user
