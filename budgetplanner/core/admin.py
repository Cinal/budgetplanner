from django.contrib import admin

from .models import Budget, SharedBudget, Transaction

admin.site.register(Budget)
admin.site.register(Transaction)
admin.site.register(SharedBudget)
