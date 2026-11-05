from django.contrib import admin

from .models import Account, Bank


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "is_active")
    search_fields = ("name", "code")


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "bank",
        "account_type",
        "opening_balance",
        "is_active",
    )

    list_filter = (
        "bank",
        "account_type",
        "is_active",
    )

    search_fields = ("name",)