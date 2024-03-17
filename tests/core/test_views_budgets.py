import pytest
from core.models import Budget, SharedBudget
from core.serializers import BudgetSerializer
from django.urls import reverse


@pytest.mark.django_db
def test__budgets(budget_factory, demo_user, request_api_with_demo_user):
    [budget_factory(user=demo_user) for _ in range(3)]
    Budget.objects.all().count()

    resp = request_api_with_demo_user(reverse("budget-list"))

    assert resp.status_code == 200
    data = resp.json()

    assert data["count"] == 3
    assert not data["next"]
    assert not data["previous"]


@pytest.mark.django_db
def test__budgets_pagination(demo_user, budget_factory, request_api_with_demo_user):
    budgets = [budget_factory(user=demo_user) for _ in range(3)]
    Budget.objects.all().count()

    resp = request_api_with_demo_user(reverse("budget-list") + "?limit=1&offset=1")
    assert resp.status_code == 200
    data = resp.json()

    assert data["count"] == 3
    assert data["previous"] == "http://testserver/api/v1/budgets/?limit=1"
    assert data["next"] == "http://testserver/api/v1/budgets/?limit=1&offset=2"

    serializer = BudgetSerializer(budgets[1])
    assert data["results"] == [serializer.data]


@pytest.mark.django_db
def test__budget_detail(budget_factory, demo_user, request_api_with_demo_user):
    budget_to_test = budget_factory(user=demo_user)

    resp = request_api_with_demo_user(reverse("budget-detail", args=[budget_to_test.id]))

    assert resp.status_code == 200
    data = resp.json()

    assert data["id"] == budget_to_test.id
    assert data["name"] == budget_to_test.name


@pytest.mark.django_db
def test__shared_budget_detail(budget_factory, shared_user, demo_user, request_api_with_demo_user):
    shared_budget = budget_factory(user=shared_user)

    SharedBudget.objects.create(budget=shared_budget, user=demo_user)

    resp = request_api_with_demo_user(reverse("budget-detail", args=[shared_budget.id]))
    assert resp.status_code == 200
    data = resp.json()

    assert data["id"] == shared_budget.id
    assert data["name"] == shared_budget.name


@pytest.mark.django_db
def test__budget_share_action(budget_factory, demo_user, shared_user, request_api_with_demo_user):
    budget_to_test = budget_factory(user=demo_user)

    resp = request_api_with_demo_user(
        url=reverse("budget-share", kwargs={"budget_id": budget_to_test.id}),
        variables={"email": shared_user.email},
        method="POST",
    )

    assert resp.status_code == 200
    data = resp.json()

    assert data["message"] == "Budget shared successfully."


@pytest.mark.django_db
def test__budget_unshare_action(
    budget_factory, shared_budget_factory, demo_user, shared_user, request_api_with_demo_user
):
    budget_to_test = budget_factory(user=demo_user)

    shared_budget_factory(budget=budget_to_test, user=shared_user)

    resp = request_api_with_demo_user(
        url=reverse("budget-unshare", kwargs={"budget_id": budget_to_test.id}),
        variables={"email": shared_user.email},
        method="POST",
    )

    assert resp.status_code == 200
    data = resp.json()

    assert data["message"] == "Budget unshared successfully."


@pytest.mark.django_db
def test__budget_share_with_none_exist_user_action(
    budget_factory, demo_user, request_api_with_demo_user
):
    budget_to_test = budget_factory(user=demo_user)

    resp = request_api_with_demo_user(
        url=reverse("budget-share", kwargs={"budget_id": budget_to_test.id}),
        variables={"email": "non-exists-user@example.com"},
        method="POST",
    )

    assert resp.status_code == 404
    data = resp.json()

    assert data["error"] == "User with this email does not exist."


@pytest.mark.django_db
def test__budget_share_action_required_field_validation(
    budget_factory, demo_user, request_api_with_demo_user
):
    budget_to_test = budget_factory(user=demo_user)

    resp = request_api_with_demo_user(
        url=reverse("budget-share", kwargs={"budget_id": budget_to_test.id}),
        method="POST",
    )

    assert resp.status_code == 400
    data = resp.json()

    assert data["error"] == "Email address is required."


@pytest.mark.django_db
def test__budget_share_action_already_shared(
    budget_factory, demo_user, request_api_with_demo_user, shared_user, shared_budget_factory
):
    budget_to_test = budget_factory(user=demo_user)
    shared_budget_factory(budget=budget_to_test, user=shared_user)

    resp = request_api_with_demo_user(
        url=reverse("budget-share", kwargs={"budget_id": budget_to_test.id}),
        variables={"email": shared_user.email},
        method="POST",
    )

    assert resp.status_code == 409
    data = resp.json()

    assert data["error"] == "Budget already shared with this user."
