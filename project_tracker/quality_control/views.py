from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.shortcuts import render
from .models import BugReport, FeatureRequest
from django.shortcuts import render, redirect
from .forms import FeedbackForm, BugReportForm, FeatureRequestForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views import View
from django.template.loader import render_to_string
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView


def index(request):
    return render(request, 'quality_control/index.html')


def bugs_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bugs_list': bugs})


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})


def features_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/features_list.html', {'features_list': features})


def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


class BugListView(ListView):
    model = BugReport
    template_name = 'quality_control/bugs_list.html'


class FeatureListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/features_list.html'


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'\



def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            recipients = ['info@example.com']
            recipients.append(email)

            send_mail(subject, message, email, recipients)

            return redirect('/quality')
    else:
        form = FeedbackForm()
    return render(request, 'quality_control/feedback.html', {'form': form})


def create_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs_list')
    else:
        form = BugReportForm
    return render(request, 'quality_control/bug_report_form.html', {'form': form})


def create_feature(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features_list')
    else:
        form = FeatureRequestForm
    return render(request, 'quality_control/feature_request_form.html', {'form': form})


class BugCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:bugs_list')


class FeatureCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:features_list')


def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', feature_id=bug_id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})


def update_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature_id=feature_id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'feature': feature})


class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bugs_list')


class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:features_list')


def delete_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bugs_list')


def delete_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect('quality_control:features_list')


class BugReportDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bugs_list')
    template_name = 'quality_control/bug_confirm_delete.html'


class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:features_list')
    template_name = 'quality_control/feature_confirm_delete.html'

# def index(request):
#     bugs_list_url = reverse('quality_control:bugs_list')
#     features_list_url = reverse('quality_control:features_list')
#     html = (f"<h1 style='color:red;'><center>Система контроля качеста</center></h1>"
#             f"<ul><li><a style='font-size:25px' href='{bugs_list_url}'>Список всех багов</a></li>"
#             f"<li><a style='font-size:25px' href='{features_list_url}'>Запросы на улучшение</a></li></ul>")
#     return HttpResponse(html)
#
#
# def bugs_list(request):
#     bugs = BugReport.objects.all()
#     bugs_html = '<h1>Список всех багов</h1><ul>'
#     for bug in bugs:
#         bugs_html += f'<li><a href="{bug.id}/" style="font-size:25px">{bug.title} - {bug.status}</a></li>'
#     bugs_html += "</ul>"
#     return HttpResponse(bugs_html)
#
#
# def features_list(request):
#     features = FeatureRequest.objects.all()
#     features_html = '<h1>Запросы на улучшение</h1><ul>'
#     for feature in features:
#         features_html += f'<li><a href="{feature.id}/" style="font-size:25px">{feature.title} - {feature.status}</a></li>'
#     features_html += "</ul>"
#     return HttpResponse(features_html)
#
#
# def bug_detail(request, bug_id):
#     bug = get_object_or_404(BugReport, id=bug_id)
#     response_html = f'<h1>{bug.title}</h1><p style="font-size:20px">{bug.description}</p>'
#     response_html += f'<h2>Принадлежит:</h2><ul><li style="font-size:20px">Проекту {bug.project}</li><li style="font-size:20px">Задаче {bug.task}</li></ul>'
#     response_html += f'<h2>Статус</h2><p style="color:green">{bug.status}</p>'
#     response_html += f'<h2>Приоритет</h2><p style="color:green">{bug.priority}<p>'
#     response_html += f'<h2>Добавлен</h2><p style="color:red">{bug.created_at}</p>'
#     response_html += f'<h2>Изменен</h2><p style="color:red">{bug.updated_at}</p>'
#     return HttpResponse(response_html)
#
#
# def feature_detail(request, feature_id):
#     feature = get_object_or_404(FeatureRequest, id=feature_id)
#     response_html = f'<h1>{feature.title}</h1><p style="font-size:20px">{feature.description}</p>'
#     response_html += (f'<h2>Принадлежит:</h2><ul><li style="font-size:20px">Проекту {feature.project}</li><li '
#                       f'style="font-size:20px">Задаче {feature.task}</li></ul>')
#     response_html += f'<h2>Статус</h2><p style="color:green">{feature.status}</p>'
#     response_html += f'<h2>Приоритет</h2><p style="color:green">{feature.priority}<p>'
#     response_html += f'<h2>Добавлен</h2><p style="color:red">{feature.created_at}</p>'
#     response_html += f'<h2>Изменен</h2><p style="color:red">{feature.updated_at}</p>'
#     return HttpResponse(response_html)
#
#
# from django.views import View
#
#
# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         bugs_list_url = reverse('quality_control:bugs_list')
#         features_list_url = reverse('quality_control:features_list')
#         html = (f"<h1 style='color:red;'><center>Система контроля качеста</center></h1>"
#                 f"<ul><li><a style='font-size:25px' href='{bugs_list_url}'>Список всех багов</a></li>"
#                 f"<li><a style='font-size:25px' href='{features_list_url}'>Запросы на улучшение</a></li></ul>")
#         return HttpResponse(html)
#
#
# from django.views.generic import ListView
#
#
# class BugsListView(ListView):
#     model = BugReport
#
#     def get(self, request, *args, **kwargs):
#         bugs = self.get_queryset()
#         bugs_html = '<h1>Список всех багов</h1><ul>'
#         for bug in bugs:
#             bugs_html += f'<li><a href="{bug.id}/">{bug.title} - {bug.status}</a></li>'
#         bugs_html += '</ul>'
#         return HttpResponse(bugs_html)
#
#
# class FeaturesListView(ListView):
#     model = FeatureRequest
#
#     def get(self, request, *args, **kwargs):
#         features = self.get_queryset()
#         features_html = '<h1>Запросы на улучшение</h1><ul>'
#         for feature in features:
#             features_html += f'<li><a href="{feature.id}/">{feature.title} - {feature.status}</a></li>'
#         features_html += '</ul>'
#         return HttpResponse(features_html)
#
#
# from django.views.generic import DetailView
#
#
# class BugsDetailView(DetailView):
#     model = BugReport
#     pk_url_kwarg = 'bug_id'
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         bug = self.object
#         response_html = f'<h1>{bug.title}</h1><p style="font-size:20px">{bug.description}</p>'
#         response_html += (f'<h2>Принадлежит:</h2><ul><li style="font-size:20px">Проекту {bug.project}</li><li '
#                           f'style="font-size:20px">Задаче {bug.task}</li></ul>')
#         response_html += f"<h2>Статус</h2><p style=\"color:green\">{bug.status}</p>"
#         response_html += f'<h2>Приоритет</h2><p style="color:green">{bug.priority}<p>'
#         response_html += f'<h2>Добавлен</h2><p style="color:red">{bug.created_at}</p>'
#         response_html += f'<h2>Изменен</h2><p style="color:red">{bug.updated_at}</p>'
#         return HttpResponse(response_html)
#
#
# class FeaturesDetailView(DetailView):
#     model = FeatureRequest
#     pk_url_kwarg = 'feature_id'
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         feature = self.object
#         response_html = f'<h1>{feature.title}</h1><p style="font-size:20px">{feature.description}</p>'
#         response_html += (f'<h2>Принадлежит:</h2><ul><li style="font-size:20px">Проекту {feature.project}</li><li '
#                           f'style="font-size:20px">Задаче {feature.task}</li></ul>')
#         response_html += f"<h2>Статус</h2><p style=\"color:green\">{feature.status}</p>"
#         response_html += f'<h2>Приоритет</h2><p style="color:green">{feature.priority}<p>'
#         response_html += f'<h2>Добавлен</h2><p style="color:red">{feature.created_at}</p>'
#         response_html += f'<h2>Изменен</h2><p style="color:red">{feature.updated_at}</p>'
#         return HttpResponse(response_html)
