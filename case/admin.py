from django.contrib import admin

from case.models import Case, Task


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
