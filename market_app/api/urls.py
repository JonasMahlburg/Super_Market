
from django.urls import path
from .views import market_view, market_single_view, sellers_view, product_view, sellers_single_view, product_single_view

urlpatterns = [
    path('market/', market_view),
    path('market/<int:pk>/', market_single_view, name='market-detail'),
    path('seller/', sellers_view),
    path('seller/<int:pk>/', sellers_single_view, name='seller_single'),
    path('product/', product_view),
    path('product/<int:pk>/', product_single_view, name='product-detail'),

]