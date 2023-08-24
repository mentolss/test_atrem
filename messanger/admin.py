from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import FeedbackUser
from django.contrib.admin import AdminSite


class ModelAdminWithoutCreation(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


# Не регистрируем стандартные модели пользователей и групп
class CustomAdminSite(AdminSite):
    site_header = 'Ваш заголовок админки'
    site_title = 'Ваш заголовок админки'
    index_title = 'Добро пожаловать в админку'


admin_site = CustomAdminSite(name='customadmin')



class FeedbackUserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'name', 'status_colored', 'timestamp')
    list_filter = ('status', 'timestamp')
    search_fields = ('name', 'phone_number')
    list_per_page = 20
    actions = ['mark_as_complete', 'mark_as_unresolved']

    def mark_as_complete(self, request, queryset):
        queryset.update(status=FeedbackUser.StatusChoices.COMPLETE)

    mark_as_complete.short_description = "Отметить как решенные"

    def mark_as_unresolved(self, request, queryset):
        queryset.update(status=FeedbackUser.StatusChoices.UNRESOLVED)

    mark_as_unresolved.short_description = "Отметить как без решения"

    def status_colored(self, obj):
        if obj.status == FeedbackUser.StatusChoices.COMPLETE:
            color = 'green'
        elif obj.status == FeedbackUser.StatusChoices.UNRESOLVED:
            color = 'red'
        else:
            color = 'orange'
        return mark_safe(
            f'<p style="color: {color}">{obj.status}</p>')

    status_colored.allow_tags = True
    status_colored.short_description = "Статус ответа на заявку"

    def phone_number(self, obj):
        return obj.phone_number

    phone_number.short_description = "Номер телефона"

    def name(self, obj):
        return obj.name

    name.short_description = "Имя"

    def timestamp(self, obj):
        return obj.timestamp

    timestamp.short_description = "Время создания"


admin_site.register(FeedbackUser, FeedbackUserAdmin)
