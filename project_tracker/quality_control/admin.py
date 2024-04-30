from django.contrib import admin
from django.core.checks import messages

from .models import BugReport, FeatureRequest


# Inline класс для модели BugReport
class BugReportInline(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('title', 'description', 'status', 'priority', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True


# Inline класс для модели BugReport
class FeatureRequestInline(admin.TabularInline):
    model = FeatureRequest
    extra = 0
    fields = ('title', 'description', 'status', 'priority', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True


@admin.action(description='Mark selected as New')
def make_new(modeladmin, request, queryset):
    queryset.update(status='New')


@admin.action(description='Mark selected as In progress')
def make_in_progress(modeladmin, request, queryset):
    queryset.update(status='In_progress')

@admin.action(description='Mark selected as Completed')
def make_completed(modeladmin, request, queryset):
    queryset.update(status='Completed')

@admin.action(description='Mark selected as Review')
def make_review(modeladmin, request, queryset):
    queryset.update(status='Review')


@admin.action(description='Mark selected as Accepted')
def make_accepted(modeladmin, request, queryset):
    queryset.update(status='Accepted')


@admin.action(description='Mark selected as Rejected')
def make_rejected(modeladmin, request, queryset):
    queryset.update(status='Rejected')


# Класс администратора для модели BugReport
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Main Information',
            {
                'fields': ['title', 'description'],
            },
        ),
        (
            'Origin',
            {
                'fields': ['project', 'task'],
            }
        ),
        (
            'Importance',
            {
                'fields': ['status', 'priority'],
            },
        ),
    ]
    list_display = ('title', 'project', 'task', 'priority', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project', 'task')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
    actions = [make_new, make_in_progress, make_completed]


# Класс администратора для модели FeatureRequest
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Main Information',
            {
                'fields': ['title', 'description'],
            },
        ),
        (
            'Origin',
            {
                'fields': ['project', 'task'],
            }
        ),
        (
            'Importance',
            {
                'fields': ['status', 'priority'],
            },
        ),
    ]
    list_display = ('title', 'project', 'task', 'priority', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project', 'task')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    actions = [make_review, make_accepted, make_rejected]