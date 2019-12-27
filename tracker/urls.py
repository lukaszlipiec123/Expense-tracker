from django.urls import path

from .import views

urlpatterns = [
    path('expenses/', views.expenses, name='expenses'),
    path('new_expense/', views.new_expense, name='new_expense'),
]
