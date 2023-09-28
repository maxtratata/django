from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    registration_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    added_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='media/products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return ''


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def __str__(self):
        return 'Order #{} on {}'.format(self.id,self.order_date)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


    def total_cost(self):
        return self.get_total_cost()




class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items' ,on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Позиция заказ'
        verbose_name_plural = 'Позиции заказа'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

