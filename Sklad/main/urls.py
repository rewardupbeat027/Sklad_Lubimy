from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

from . import views
from django.urls import path
from .views import SearchResultsView, SearchResultsView_Detail, SearchResultsView_Employee

urlpatterns = [path('', views.main, name="main"),
               path('register/', views.register, name='register'),
               path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
               path('profile/', views.profile, name='profile'),
               path('employee/', views.employee, name='employee'),
               path('inventar_forms/', views.inventar_forms, name='inventar_forms'),
               path('employee_forms/', views.employee_forms, name='employee_forms'),
               path('category_forms/', views.category_forms, name='category_forms'),
               path('inventar/', views.inventar, name='inventar'),
               path('inventar_AZ/', views.inventar_AZ, name='inventar_AZ'),
               path('inventar_ZA/', views.inventar_ZA, name='inventar_ZA'),
               path('inventar_price/', views.inventar_price, name='inventar_price'),
               path('inventar_reprice/', views.inventar_reprice, name='inventar_reprice'),
               path('inventar_detail_AZ/<int:category_id>', views.inventar_AZ_cat, name='inventar_AZ_cat'),
               path('inventar_detail_ZA/<int:category_id>', views.inventar_ZA_cat, name='inventar_ZA_cat'),
               path('inventar_detail_price/<int:category_id>', views.inventar_price_cat, name='inventar_price_cat'),
               path('inventar_detail_reprice/<int:category_id>', views.inventar_reprice_cat,
                    name='inventar_reprice_cat'),
               path('inventar_detail/<int:category_id>', views.inventar_detail, name='inventar_detail'),
               path('inventar/<int:pk>', views.MyDetailView1.as_view(), name='detail'),
               path('categories/', views.categories, name='categories'),
               path('search/', SearchResultsView, name='search_results'),
               path('search_in_categories/<int:category_id>', SearchResultsView_Detail, name='search_results_detail'),
               path('search_in_employee/', SearchResultsView_Employee, name='search_results_employee'),

               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
