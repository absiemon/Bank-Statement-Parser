from django.urls import path
from . import views

urlpatterns = [
    path('bank-statements/', views.BankStatementList.as_view(), name='bank-statement-list'),
    path('bank-statements/search/', views.TransactionSearch.as_view(), name='transaction-search'),
    path('bank-statements/search-by-date/', views.GetTransactionByDate.as_view(), name='get-transaction-by-date'),
    
]