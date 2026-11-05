from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    color = models.CharField(max_length=7, blank=True)
    logo = models.CharField(max_length=255, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"

    def __str__(self):
        return self.name

class AccountType(models.TextChoices):
    CURRENT = "CURRENT", "Cuenta corriente"
    SAVINGS = "SAVINGS", "Cuenta ahorro"
    TAX = "TAX", "Impuestos"
    CASH = "CASH", "Efectivo"
    INVESTMENT = "INVESTMENT", "Inversión"


class Account(models.Model):
    bank = models.ForeignKey(
        Bank,
        on_delete=models.PROTECT,
        related_name="accounts",
    )

    name = models.CharField(max_length=100)

    account_type = models.CharField(
        max_length=20,
        choices=AccountType.choices,
        default=AccountType.CURRENT,
    )

    opening_balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    opening_balance_date = models.DateField()

    currency = models.CharField(
        max_length=3,
        default="EUR",
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["bank", "name"]
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"

    def __str__(self):
        return f"{self.bank.name} · {self.name}"