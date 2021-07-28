from django.db import models


STATUS = (('ACTIVE', 'АКТИВНЫЙ'),
          ('CLOSED','НЕАКТИВНЫЙ'))

STATUS_DISCOUNT = (('RESERVED', 'зарезервировано',
                    'ACTIVATED','активирован'))




TYPE_NETWORK = (('INSTAGRAM','i'),
                ('VKONTAKTE','v'),
                ('FACEBOOK','f'),)



class Discriptions(models.Model):
    discriptions = models.TextField('Условия')
    active = models.BooleanField(default=True)




class Discount(models.Model):
    start_date = models.DateField('Дата начало')
    end_date = models.DateField('Дата окончания')
    percent = models.IntegerField('Процент скидки')
    status = models.CharField(max_length=10, choices=STATUS)
    discric = models.ForeignKey(Discriptions, on_delete=models.CASCADE)
    order_num = models.IntegerField()





class Categori(models.Model):
    name = models.CharField('Название категории', max_length=20)
    order_num = models.IntegerField('Очередность')
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField('Название компании', max_length=30)
    photo = models.URLField()
    description = models.TextField('Описание компании')
    working_hours = models.CharField('Рабочие часы', max_length=20)
    pin = models.CharField('Пин-код', max_length=4)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    categori  = models.ForeignKey(Categori, on_delete=models.CASCADE)
    adress = models.ForeignKey('Adress', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # @property
    # def discount(self):
    #     return Discount.objects.get(id=self.id).percent
    #
    # @property
    # def city(self):
    #     return City.objects.get(id=self.id).name
    #
    # @property
    # def view(self):
    #     return View.objects.get(id=self.id).count

    # @property
    # def social(self):
    #     return SocialNetworks.objects.filter(company=self)

class SocialNetworks(models.Model):
    urls = models.URLField()
    type = models.CharField(max_length=20, choices=TYPE_NETWORK)
    logo = models.URLField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)





class City(models.Model):
    name = models.CharField('Название города',max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Adress(models.Model):
    adress = models.CharField('Адресс',max_length=50)
    longitude = models.CharField('Долгота',max_length=100)
    latitude = models.CharField('Широта', max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.adress


class Phone(models.Model):
    number = models.CharField('Номер телефона', max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)



class View(models.Model):
    count = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Review(models.Model):
    review = models.TextField('Отзыв от клиента')
    date_time = models.DateField(auto_now=True)
    name = models.CharField(max_length=30, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class ClientDiscount(models.Model):
    add_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS, verbose_name='Статус')
    edit_date = models.DateField()
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    client = models.ForeignKey('Client',on_delete=models.CASCADE)



class Client(models.Model):
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone_number







