from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Delivery(models.Model):
    # Fields from Cargo
    product_name = models.CharField("Наименование товара", max_length=255, help_text="Здесь вводится наименование товара или продукта, который будет отправлен. В нашем примере это 'Краска Мемби'.")
    weight = models.FloatField("Вес груза", help_text="Указывается вес груза, который отправляется. Например, '2' может означать 2 кг.")
    volume = models.FloatField("Объем груза", null=True, blank=True, help_text='Здесь указывается объем груза в кубических метрах или другой единице измерения. Например, "2" может быть 2 куб. м.')
    quantity = models.PositiveIntegerField(
        "Количество единиц товара", null=True, blank=True, help_text='Общее количество товара или продукта. Например, "100" банок краски.')
    document = models.FileField(
        "PDF документ", upload_to="cargo_documents/", null=True, blank=True, help_text='Здесь можно загрузить документацию или иную важную информацию, связанную с грузом.')

    # Fields from Address
    address_line = models.TextField("Адрес", help_text='Указывается адрес, откуда будет забираться груз.')
    delivery_address = models.TextField("Доставка", help_text='Адрес, куда груз будет доставлен.')
    additional_info = models.TextField(
        "Дополнительная информация", null=True, blank=True, help_text='Любая дополнительная информация, которую следует учитывать при отправке или доставке.')

    # Fields from ServiceRequirements
    INSURANCE_CHOICES = (('yes', 'Да'), ('no', 'Нет'))
    insurance_needed = models.CharField(
        "Необходимость страхования груза", max_length=3, choices=INSURANCE_CHOICES, default="Нет", help_text='Выберите "Да", если груз нуждается в страховании, и "Нет", если нет.')
    storage = models.BooleanField("Необходимость хранения", default=False, help_text='Отметьте, если необходимо временное хранение груза перед отправкой или после доставки.')
    customs_clearance = models.BooleanField(
        "Таможенное оформление", default=False, help_text='Отметьте, если груз требует таможенного оформления.')
    packaging = models.BooleanField("Упаковка", default=False, help_text='Отметьте, если необходимо особое упаковывание груза.')
    special_requirements = models.TextField(
        "Особые требования", null=True, blank=True, help_text='Любые дополнительные требования или заметки к грузу.')

    # Fields from ContactInformation
    full_name = models.CharField("Полное имя", max_length=255, help_text='Имя отправителя или контактного лица. Например, "Marselle".')
    company_name = models.CharField(
        "Наименование компании", max_length=255, null=True, blank=True, help_text='Название компании отправителя. Например, "Remalux".')
    phone_number = models.CharField("Контактный номер телефона", max_length=20, help_text='Телефон для связи. Например, "+7747***9991".')
    email = models.EmailField("Адрес электронной почты", help_text='Электронный адрес отправителя для уведомлений или связи.')

    # Additional fields
    desired_departure_date = models.DateField("Желаемая дата отправления", help_text='Дата, когда отправитель хочет, чтобы груз был отправлен.')
    delivery_deadline = models.DateField(
        "Сроки доставки", null=True, blank=True, help_text='Желаемая дата доставки груза.')
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.product_name} - {self.user.username} | От {self.address_line} до {self.delivery_address} | Создано: {self.created_at.strftime('%Y.%m.%d %H:%M:%S')}"


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    excerpt = models.TextField(verbose_name="Отрывок", blank=True)
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Автор")
    image = models.ImageField(upload_to='news_images/', null=True, blank=True, verbose_name="Изображение")
    
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
        ('archived', 'Архив'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="Статус")
    
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    tags = models.ManyToManyField('Tag', blank=True, verbose_name="Теги")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['-created_at']


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ['-created_at']


class Support(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name="Имя",
        help_text="Введите ваше полное имя."
    )
    email = models.EmailField(
        verbose_name="Адрес электронной почты",
        help_text="Введите адрес вашей электронной почты, чтобы мы могли связаться с вами."
    )
    message = models.TextField(
        verbose_name="Сообщение", 
        max_length=1000,
        help_text="Опишите вашу проблему или вопрос. Максимальная длина сообщения - 1000 символов."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания",
        help_text="Дата и время, когда обращение было создано."
    )

    class Meta:
        verbose_name = "Поддержка"
        verbose_name_plural = "Поддержки"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email} - {self.created_at}"

    

class Schedule_of_road_transport(models.Model):
    file_and_photo = models.FileField("PDF или IMG документ", upload_to="Schedule_of_road_transport_documents/", null=True, blank=True, help_text='Загрузите PDF или изображение (IMG) документа, содержащего информацию о графике дорожного транспорта. Разрешены файлы в форматах PDF или изображений (например, JPG, PNG).')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Получатель")
    application = models.ForeignKey(Delivery, on_delete=models.CASCADE, verbose_name="Заявка")
    data = models.DateField(verbose_name="Дата отправки")
    additional_info = models.TextField("Дополнительная информация", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "График автоперевозок"
        verbose_name_plural = "График автоперевозок"
        ordering = ['-created_at']
    
    def __str__(self) -> str:
        return f"Заявка: {self.application.product_name} Получатель: {self.recipient.username} Дата отправки: {self.data}"