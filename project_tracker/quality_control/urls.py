from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bugs_list, name='bugs_list'),  # новый маршрут
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('features/', views.features_list, name='features_list'),  # новый маршрут
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('bugs/new/', views.create_bug, name='create_bug'),
    path('features/new/', views.create_feature, name='create_feature'),
    path('bugs/create/', views.BugCreateView.as_view(), name='create_bug'),
    path('features/create/', views.FeatureCreateView.as_view(), name='create_feature'),
    path('bugs/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    path('features/<int:features_id>/update/', views.update_feature, name='update_feature'),
    path('bugs/<int:bug_id>/update/', views.BugReportUpdateView.as_view(), name='update_bug'),
    path('features/<int:features_id>/update/', views.FeatureRequestUpdateView.as_view(), name='update_feature'),
    path('bugs/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),
    path('features/<int:feature_id>/delete/', views.delete_feature, name='delete_feature'),
    path('bugs/<int:bug_id>/delete/', views.BugReportDeleteView.as_view(), name='delete_bug'),
    path('features/<int:feature_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='delete_feature'),

#     path('', views.IndexView.as_view(), name='index'),
#     path('bugs/', views.BugsListView.as_view(), name='bugs_list'),
#     path('bugs/<int:bug_id>/', views.BugsDetailView.as_view(), name='bug_detail'),
#     path('features/', views.FeaturesListView.as_view(), name='features_list'),
#     path('features/<int:feature_id>/', views.FeaturesDetailView.as_view(), name='features_detail'),
]
