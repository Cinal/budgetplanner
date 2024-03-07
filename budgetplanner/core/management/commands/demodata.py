from core.constants import CategoryChoices
from core.models import Budget, BudgetUser, SharedBudget, Transaction
from django.core.management.base import BaseCommand

DEMODATA_IDS = {
    "user": {
        "default": {
            "id": 100,
            "email": "default@budgetplanner.com",
            "password": "budget",
            "phone_number": "487111222333",
        },
        "first": {
            "id": 101,
            "email": "first@budgetplanner.com",
            "password": "budget",
        },
    },
    "budget": {
        "default": {"id": 10, "name": "Family", "user": 100},
        "first": {"id": 11, "name": "Prosperity", "user": 101},
        "second": {"id": 12, "name": "School", "user": 100},
    },
    "transaction": [
        {
            "budget_id": 10,
            "category": CategoryChoices.UTILITIES,
            "amount": 50.00,
            "currency": "USD",
            "description": "Weekly groceries",
            "date": "2024-03-01",
        },
        {
            "budget_id": 11,
            "category": CategoryChoices.FOOD,
            "amount": 12.00,
            "currency": "USD",
            "description": "Weekly groceries",
            "date": "2024-03-01",
        },
        {
            "budget_id": 12,
            "category": CategoryChoices.ENTERTAINMENT,
            "amount": 123.00,
            "currency": "USD",
            "description": "Weekly groceries",
            "date": "2024-03-01",
        },
    ],
}


class Command(BaseCommand):
    help = "Demodata"

    def handle(self, *args, **options):
        self.create_demodata()

    def generate_users(self):
        print("Generatting users")
        user_data = [DEMODATA_IDS["user"]["default"], DEMODATA_IDS["user"]["first"]]
        for user_info in user_data:
            user = BudgetUser(
                first_name="John", last_name="Bravo", email=user_info["email"], is_superuser=False
            )

            user.pk = user_info["id"]
            user.set_password(user_info["password"])
            user.save()

    def generate_budgets(self):
        print("Generatting budgets")
        budget_data = [
            DEMODATA_IDS["budget"]["default"],
            DEMODATA_IDS["budget"]["first"],
            DEMODATA_IDS["budget"]["second"],
        ]
        for budget_value in budget_data:
            user_instance = BudgetUser.objects.get(pk=budget_value["user"])
            Budget.objects.create(
                id=budget_value["id"], name=budget_value["name"], user=user_instance
            )

    def generate_transactions(self):
        print("Generatting transactions")
        transactions_data = DEMODATA_IDS["transaction"]
        for transaction_info in transactions_data:
            budget_instance = Budget.objects.get(pk=int(transaction_info["budget_id"]))
            Transaction.objects.create(
                budget=budget_instance,
                category=transaction_info["category"],
                amount=transaction_info["amount"],
                currency=transaction_info["currency"],
                description=transaction_info["description"],
                date=transaction_info["date"],
            )

    def generate_sharedbudget(self):
        print("Generatting sharedbudget")
        shared_budgets_data = [
            {
                "budget_id": 10,
                "user_id": 101,
            },
        ]
        for shared_budget_info in shared_budgets_data:
            budget_instance = Budget.objects.get(pk=shared_budget_info["budget_id"])
            user_instance = BudgetUser.objects.get(pk=shared_budget_info["user_id"])
            SharedBudget.objects.create(budget=budget_instance, user=user_instance)

    def create_demodata(self):
        self.generate_users()
        self.generate_budgets()
        self.generate_transactions()
        self.generate_sharedbudget()
        print("Done!")
