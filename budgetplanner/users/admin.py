from django.contrib import admin

from .models import BudgetUser


class BudgetUserAdmin(admin.ModelAdmin):
    list_display = ("id", "email")


admin.site.register(BudgetUser, BudgetUserAdmin)
