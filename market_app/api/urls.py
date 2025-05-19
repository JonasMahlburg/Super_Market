
from django.urls import path
from .views import Marketsview, market_view, market_single_view, Sellersview, sellers_view, sellers_single_view,  Productsview, product_view, product_single_view

urlpatterns = [
    path('market/', Marketsview.as_view()),
    path('market/<int:pk>/', market_single_view, name='market-detail'),
    path('seller/', Sellersview.as_view()),
    path('seller/<int:pk>/', sellers_single_view, name='seller_single'),
    path('product/', Productsview.as_view()),
    path('product/<int:pk>/', product_single_view, name='product-detail'),

]