
from django.urls import path
from .views import Marketsview, MarketDetail, MarketSingleView, market_view, market_single_view, \
                   Sellersview, SellerDetail, sellers_view, sellers_single_view, \
                   Productsview, ProductDetail, product_view, product_single_view

urlpatterns = [
    path('market/', Marketsview.as_view()),
    path('market/<int:pk>/', MarketSingleView.as_view(), name='market-detail'),
    path('seller/', Sellersview.as_view()),
    path('seller/<int:pk>/', SellerDetail.as_view(), name='seller_detail'),
    path('product/', Productsview.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),

]