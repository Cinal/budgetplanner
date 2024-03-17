import pytest
from core.serializers import SharedBudgetSerializer, TransactionSerializer
from django.urls import reverse


@pytest.mark.django_db
def test__transactions(demo_user, transaction_factory, budget_factory, request_api_with_demo_user):
    demo_user_budget = budget_factory(user=demo_user)
    [transaction_factory(budget=demo_user_budget) for _ in range(3)]

    resp = request_api_with_demo_user(reverse("transaction-list"))
    assert resp.status_code == 200
    data = resp.json()

    assert data["count"] == 3
    assert not data["next"]
    assert not data["previous"]


@pytest.mark.django_db
def test__transactions_pagination(
    demo_user, transaction_factory, budget_factory, request_api_with_demo_user
):
    demo_user_budget = budget_factory(user=demo_user)
    transactions = [transaction_factory(budget=demo_user_budget) for _ in range(3)]

    resp = request_api_with_demo_user(reverse("transaction-list") + "?limit=1&offset=1")
    assert resp.status_code == 200
    data = resp.json()

    assert data["count"] == 3
    assert data["previous"] == "http://testserver/api/v1/transactions/?limit=1"
    assert data["next"] == "http://testserver/api/v1/transactions/?limit=1&offset=2"

    serializer = TransactionSerializer(transactions[1])
    assert data["results"] == [serializer.data]


@pytest.mark.django_db
def test__shared_budgets(shared_budget_factory, request_api_with_demo_user):
    [shared_budget_factory() for _ in range(3)]

    resp = request_api_with_demo_user(
        reverse("shared-budget-list"),
    )
    assert resp.status_code == 200
    data = resp.json()

    assert data["count"] == 3
    assert not data["next"]
    assert not data["previous"]


@pytest.mark.django_db
def test__shared_budgets_pagination(shared_budget_factory, request_api_with_demo_user):
    shared_budgets = [shared_budget_factory() for _ in range(3)]

    resp = request_api_with_demo_user(
        reverse("shared-budget-list") + "?limit=1&offset=1",
    )
    assert resp.status_code == 200
    data = resp.json()

    assert data["count"] == 3
    assert data["previous"] == "http://testserver/api/v1/shared-budgets/?limit=1"
    assert data["next"] == "http://testserver/api/v1/shared-budgets/?limit=1&offset=2"

    serializer = SharedBudgetSerializer(shared_budgets[1])
    assert data["results"] == [serializer.data]
