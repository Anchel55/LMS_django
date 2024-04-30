from django.db import models
from tasks.models import Project, Task


class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    PRIORITY_CHOICES = [
        ('High', 'Высокий'),
        ('Lower-high', 'Выше среднего'),
        ('Medium', 'Средний'),
        ('Lower-middle', 'Ниже среднего'),
        ('Low', 'Низкий')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(
        Project,
        related_name='bug_reports_as_project',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='bug_reports_as_task',
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES,
        default='High'
    )

    def __str__(self):
        return self.title


class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('Review', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
    PRIORITY_CHOICES = [
        ('High', 'Высокий'),
        ('Lower-high', 'Выше среднего'),
        ('Medium', 'Средний'),
        ('Lower-middle', 'Ниже среднего'),
        ('Low', 'Низкий')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(
        Project,
        related_name='feature_requests_as_project',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='feature_requests_as_task',
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Review',
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES,
        default='High'
    )

    def __str__(self):
        return self.title