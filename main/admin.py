from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Category, Delivery, News, Support, Tag, Schedule_of_road_transport


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date',
                    'status', 'category', 'views_count', 'get_image')
    list_filter = ('published_date', 'status', 'category', 'tags')
    search_fields = ('title', 'content')
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150px" />')
        return 'Not image'

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = [
        "product_name", "weight", "address_line", "delivery_address",
        "desired_departure_date", "delivery_deadline", "created_at", "document_preview"
    ]
    search_fields = ["product_name", "address_line",
                    "delivery_address", "full_name"]
    list_filter = ["desired_departure_date", "created_at",
                "insurance_needed", "storage", "customs_clearance", "packaging"]
    list_editable = ["desired_departure_date", "delivery_deadline"]
    ordering = ['-created_at']

    def document_preview(self, obj):
        if obj.document:
            return format_html('<a href="{}">Просмотреть документ</a>', obj.document.url)
        return "Документ отсутствует"
    document_preview.short_description = 'PDF документ'


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = [
        "name", "email", "message", "created_at"
    ]
    search_fields = ["name", "email", "message"]
    list_filter = ["email", "created_at"]
    ordering = ['-created_at']


@admin.register(Schedule_of_road_transport)
class ScheduleOfRoadTransportAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'application', 'data', 'document_preview', 'created_at')
    list_filter = ('recipient', 'data', 'created_at')
    search_fields = ('recipient__username', 'application__product_name', 'additional_info')
    date_hierarchy = 'data'
    ordering = ('-created_at',)
    raw_id_fields = ('recipient', 'application')

    def document_preview(self, obj):
        if obj.file_and_photo:
            return format_html(f'<a href="{obj.file_and_photo.url}">Просмотреть документ</a>')
        return "Документ отсутствует"

    document_preview.short_description = 'PDF документ'