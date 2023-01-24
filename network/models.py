from django.db import models


class Contacts(models.Model):
    email = models.EmailField(verbose_name="Электронная почта", max_length=50, unique=True)
    country = models.CharField(verbose_name="Страна", max_length=60)
    city = models.CharField(verbose_name="Город", max_length=60)
    street = models.CharField(verbose_name="Улица", max_length=60)
    number_home = models.CharField(verbose_name="Дом", max_length=10)

    def __str__(self):
        return f"{self.email}, {self.country}, {self.city}, {self.street}, {self.number_home}"


class Products(models.Model):
    title = models.CharField(verbose_name="Название", max_length=60)
    model = models.CharField(verbose_name="Модель", max_length=60)
    data = models.DateField(verbose_name="Дата поступления в продажу", max_length=10)

    def __str__(self):
        return f"{self.title}, {self.model}, {self.data}"


class Network(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100)
    contacts = models.ForeignKey("Contacts", verbose_name="Контакты", on_delete=models.CASCADE)
    products = models.ForeignKey("Products", verbose_name="Продукция", on_delete=models.CASCADE)
    supplier = models.ForeignKey("Network", verbose_name="Поставщик", on_delete=models.CASCADE, null=True)
    arrears = models.FloatField(verbose_name="Задолженность", null=True)
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
