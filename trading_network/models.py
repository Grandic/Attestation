from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Link(models.Model):
    """Trade network"""
    name = models.CharField(max_length=250, verbose_name='Наименование')
    supplier = models.ForeignKey(to='self', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Поставщик')

    network_levels = [
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    ]

    level = models.IntegerField(choices=network_levels, verbose_name='Уровень', null=True, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True, blank=True)
    debt_to_supplier = models.DecimalField(max_digits=15, decimal_places=2,
                                           verbose_name='Задолженность перед поставщиком', null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name='email')
    country = models.CharField(max_length=250, verbose_name='Страна', null=True, blank=True)
    city = models.CharField(max_length=250, verbose_name='Город', null=True, blank=True)
    street = models.CharField(max_length=250, verbose_name='Улица', null=True, blank=True)
    house_number = models.CharField(max_length=20, verbose_name='Номер дома', null=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.country}, {self.city}'

    class Meta:
        verbose_name = 'Элемент торговой сети'
        verbose_name_plural = 'Элементы торговой сети'


@receiver(pre_save, sender=Link)
def set_rank(instance, **kwargs):
    """Установка уровня"""
    if instance.contractor:
        if instance.contractor.rank == 2 or instance.contractor.rank == 1:
            instance.rank = 2
        else:
            instance.rank = 1
    else:
        instance.rank = 0


class Product(models.Model):
    """Продукты"""
    name = models.CharField(max_length=250, verbose_name='Наименование')
    model = models.CharField(max_length=150, verbose_name='Модель', null=True, blank=True)
    contractor = models.ForeignKey(Link, on_delete=models.CASCADE, verbose_name='торговая сеть')
    release_date = models.DateTimeField(verbose_name='Дата выхода', null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='цена', null=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
