from core.constants import CategoryChoices, CurrencyChoices
from django.db import models
from users.models import BudgetUser

# class BudgetUser(AbstractUser):
#     username = None
#     email = models.EmailField(_("email address"), unique=True)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
#     # username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#     # email = models.EmailField(_('email address'), unique = True)
#     # # username = models.CharField(max_length=254, null=True, blank=True)
#     # email = models.CharField(max_length=255, unique=True)
#     # first_name = models.CharField(max_length=254, null=True, blank=True)
#     # last_name = models.CharField(max_length=254, null=True, blank=True)
#     # password = models.CharField(max_length=255)
#     # is_superuser = models.BooleanField(default=False)
#     # # is_stuff = models.BooleanField(default=False)

#     # groups = models.ManyToManyField(
#     #     Group,
#     #     verbose_name=_("Groups"),
#     #     blank=True,
#     #     related_name='budgetplanner_user_set',
#     # )
#     # user_permissions = models.ManyToManyField(
#     #     Permission,
#     #     verbose_name=_('User permissions'),
#     #     blank=True,
#     #     related_name='budgetplanner_user_set',
#     # )
#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     EMAIL_FIELD = 'email'

#     def __str__(self):
#         return self.name

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin

# class Meta:
#     db_table = 'auth_user'


class Budget(models.Model):
    user = models.ForeignKey(BudgetUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CategoryChoices.choices())
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CurrencyChoices.choices())
    description = models.TextField(null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.amount} {self.currency}"


class SharedBudget(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    user = models.ForeignKey(BudgetUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.budget} shared with {self.user}"
