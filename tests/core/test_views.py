import pytest
from core.models import Budget, SharedBudget, Transaction
from core.serializers import BudgetSerializer, SharedBudgetSerializer, TransactionSerializer
from django.urls import reverse


@pytest.mark.django_db
def test__budgets(client, budget_factory):
    [budget_factory() for _ in range(3)]
    Budget.objects.all().count()

    resp = client.get(
        reverse("budget-list"),
        content_type="application/json",
    )
    assert resp.status_code == 200
    data = resp.json()

    assert data["count"] == 3
    assert not data["next"]
    assert not data["previous"]


@pytest.mark.django_db
def test__budgets_pagination(client, budget_factory):
    budgets = [budget_factory() for _ in range(3)]
    Budget.objects.all().count()

    resp = client.get(
        reverse("budget-list") + "?limit=1&offset=1",
        content_type="application/json",
    )
    assert resp.status_code == 200
    data = resp.json()

    assert data["count"] == 3
    assert data["previous"] == "http://testserver/api/v1/budgets/?limit=1"
    assert data["next"] == "http://testserver/api/v1/budgets/?limit=1&offset=2"

    serializer = BudgetSerializer(budgets[1])
    assert data["results"] == [serializer.data]


@pytest.mark.django_db
def test__transactions(client, transaction_factory):
    [transaction_factory() for _ in range(3)]
    Transaction.objects.all().count()

    resp = client.get(
        reverse("transaction-list"),
        content_type="application/json",
    )
    assert resp.status_code == 200
    data = resp.json()

    assert data["count"] == 3
    assert not data["next"]
    assert not data["previous"]


@pytest.mark.django_db
def test__transactions_pagination(client, transaction_factory):
    transactions = [transaction_factory() for _ in range(3)]
    Transaction.objects.all().count()

    resp = client.get(
        reverse("transaction-list") + "?limit=1&offset=1",
        content_type="application/json",
    )
    assert resp.status_code == 200
    data = resp.json()

    assert data["count"] == 3
    assert data["previous"] == "http://testserver/api/v1/transactions/?limit=1"
    assert data["next"] == "http://testserver/api/v1/transactions/?limit=1&offset=2"

    serializer = TransactionSerializer(transactions[1])
    assert data["results"] == [serializer.data]


@pytest.mark.django_db
def test__shared_budgets(client, shared_budget_factory):
    [shared_budget_factory() for _ in range(3)]
    SharedBudget.objects.all().count()

    resp = client.get(
        reverse("shared-budget-list"),
        content_type="application/json",
    )
    assert resp.status_code == 200
    data = resp.json()

    assert data["count"] == 3
    assert not data["next"]
    assert not data["previous"]


@pytest.mark.django_db
def test__shared_budgets_pagination(client, shared_budget_factory):
    shared_budgets = [shared_budget_factory() for _ in range(3)]
    SharedBudget.objects.all().count()

    resp = client.get(
        reverse("shared-budget-list") + "?limit=1&offset=1",
        content_type="application/json",
    )
    assert resp.status_code == 200
    data = resp.json()

    assert data["count"] == 3
    assert data["previous"] == "http://testserver/api/v1/shared-budgets/?limit=1"
    assert data["next"] == "http://testserver/api/v1/shared-budgets/?limit=1&offset=2"

    serializer = SharedBudgetSerializer(shared_budgets[1])
    assert data["results"] == [serializer.data]
