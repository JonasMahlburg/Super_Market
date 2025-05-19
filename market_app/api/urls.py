
from django.urls import path, include
from .views import Marketsview, MarketDetail, MarketSingleView, SellerOfMarketList, market_single_view, \
                   Sellersview, SellerDetail, sellers_view, sellers_single_view, \
                   Productsview, ProductDetail, ProductViewSet, product_view, product_single_view
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('market/', Marketsview.as_view()),
    path('market/<int:pk>/', MarketSingleView.as_view(), name='market-detail'),
    path('market/<int:pk>/sellers/', SellerOfMarketList.as_view()),
    path('seller/', Sellersview.as_view()),
    path('seller/<int:pk>/', SellerDetail.as_view(), name='seller-detail'),
    path('product/', Productsview.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),

]