from django.contrib import admin

from .models import Budget, SharedBudget, Transaction


class BudgetAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user", "created_at")


admin.site.register(Budget, BudgetAdmin)
admin.site.register(Transaction)
admin.site.register(SharedBudget)
