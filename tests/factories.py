import factory
from core.models import Budget, SharedBudget, Transaction
from faker import Faker
from users.models import BudgetUser

fake = Faker()


class BudgetUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BudgetUser

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = factory.LazyAttribute(lambda _: fake.unique.email())


class BudgetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Budget

    user = factory.SubFactory(BudgetUserFactory)
    name = factory.LazyAttribute(lambda n: fake.word()[:200])


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    budget = factory.SubFactory(BudgetFactory)
    category = factory.Faker("word")
    amount = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)
    currency = factory.Faker("currency_code")
    description = factory.Faker("text")
    date = factory.Faker("date_object")


class SharedBudgetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SharedBudget

    budget = factory.SubFactory(BudgetFactory)
    user = factory.SubFactory(BudgetUserFactory)
