from functools import partial
from typing import Dict, Optional, Union

import pytest
from core.models import Budget, BudgetUser
from django.http import HttpResponse
from django.test import Client as DjangoTestClient
from pytest_factoryboy import register
from rest_framework_simplejwt.tokens import RefreshToken

from tests.factories import (
    BudgetFactory,
    BudgetUserFactory,
    SharedBudgetFactory,
    TransactionFactory,
)

Primitives = Union[str, int, bool]
VariableValues = Dict[str, Primitives]


def _request_api(
    url: str,
    variables: Optional[VariableValues] = None,
    method: str = "GET",
    token: Optional[str] = None,
) -> HttpResponse:
    headers: Dict[str, str] = {}

    if token:
        headers["HTTP_AUTHORIZATION"] = f"Bearer {token}"
    client = DjangoTestClient(**headers)

    if method.upper() == "POST":
        print("lazl")
        print(headers)
        response = client.post(
            url,
            data=variables,
            content_type="application/json",
            **headers,
        )
    elif method == "PUT":
        response = client.put(url, data=variables, content_type="application/json", **headers)
    elif method == "DELETE":
        response = client.delete(url, **headers)
    else:
        response = client.get(
            url,
            data=variables,
            **headers,
        )
    return response


@pytest.fixture
def request_api_with_demo_user(token_for_demo_user):
    return partial(_request_api, token=token_for_demo_user)


@pytest.fixture
def token_for_demo_user(demo_user):
    refresh = RefreshToken.for_user(demo_user)
    return str(refresh.access_token)


@pytest.fixture
def demo_user():
    demo_user, _ = BudgetUser.objects.update_or_create(email="demoapi@example.com", is_staff=True)
    demo_user.set_password("12345")
    demo_user.save()
    return demo_user


@pytest.fixture
def shared_user():
    demo_user, _ = BudgetUser.objects.update_or_create(
        email="demoshared_user@example.com", is_staff=True
    )
    demo_user.set_password("12345")
    demo_user.save()
    return demo_user


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
