import pytest
from core.models import Budget
from django.urls import reverse


@pytest.mark.django_db
def test__budgets_pagination(client):
    total_results = Budget.objects.all().count()

    resp = client.get(
        reverse("budget-list"),
        content_type="application/json",
    )
    assert resp.status_code == 200
    data = resp.json()

    assert data["count"] == total_results
    assert not data["next"]
    assert not data["previous"]
