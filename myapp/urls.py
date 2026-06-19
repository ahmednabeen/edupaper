from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('papers/internship/', views.paper_list, {'category': 'internship'}, name='paper_internship'),
    path('papers/thesis/', views.paper_list, {'category': 'thesis'}, name='paper_thesis'),
    path('papers/term/', views.paper_list, {'category': 'term'}, name='paper_term'),
    path('papers/project/', views.paper_list, {'category': 'project'}, name='paper_project'),
    path('papers/', views.paper_list, name='paper_list'),
    path('papers/<slug:slug>/', views.paper_detail, name='paper_detail'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_post, name='blog_post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-conditions/', views.terms_conditions, name='terms_conditions'),
    path('scholarship/', views.all_scholarships, name='all_scholarships'),
    path('scholarship/<slug:region>/<slug:country>/<slug:slug>/', views.scholarship_detail, name='scholarship_detail'),
    path('scholarship/<slug:region>/<slug:country>/', views.scholarship_country, name='scholarship_country'),
    path('scholarship/<slug:region>/', views.scholarship_list, name='scholarship_list'),
]
