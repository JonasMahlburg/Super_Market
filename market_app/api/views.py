from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MarketSerializer, SellerSerializer, ProductSerializer, MarketHyperlinkedSerializer, ProductHyperlinkSerializer
from market_app.models import Market, Seller, Product
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


class Marketsview(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@api_view(['GET', 'POST'])
def market_view(request):
   if request.method == 'GET':
       markets = Market.objects.all()
       serializer = MarketHyperlinkedSerializer(markets, many=True, context={'request': request}, fields = ['id', 'name', 'location'])
       return Response(serializer.data)
   
   if request.method == 'POST':
      serializer = MarketSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

@api_view(['GET', 'DELETE', 'PUT'])
def market_single_view(request, pk):
   if request.method == 'GET':
       market = Market.objects.get(pk=pk)
       serializer = MarketSerializer(market, context={'request': request})
       return Response(serializer.data)
   
   if request.method == 'PUT':
       market = Market.objects.get(pk=pk)
       serializer = MarketSerializer(market, data=request.data, partial=True)
       if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
       else:
         return Response(serializer.errors)
   
   if request.method == 'DELETE':
       market = Market.objects.get(pk=pk)
       serializer = MarketSerializer(market)
       market.delete()
       return Response(serializer.data)
   

class MarketDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class Sellersview(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@api_view(['GET', 'POST'])
def sellers_view(request):
   if request.method == 'GET':
       sellers = Seller.objects.all()
       serializer = SellerSerializer(sellers, many=True)
       return Response(serializer.data)
   
   if request.method == 'POST':
      serializer = SellerSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      else:
         return Response(serializer.errors)
      

@api_view()
def sellers_single_view(request, pk):

   if request.method == 'GET':
       seller = Seller.objects.get(pk=pk)
       serializer = SellerSerializer(seller)
       return Response(serializer.data)


class SellerDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class Productsview(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

@api_view(['GET', 'POST'])
def product_view(request):
   if request.method == 'GET':
       products = Product.objects.all()
       serializer = ProductHyperlinkSerializer(products, many=True, context={'request': request}, fields = ['id', 'name', 'price'] )
       return Response(serializer.data)
   
   if request.method == 'POST':
      serializer = ProductSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      else:
         return Response(serializer.errors)
      

class ProductDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

      
@api_view(['GET', 'DELETE', 'PUT'])
def product_single_view(request, pk):
   if request.method == 'GET':
       product = Product.objects.get(pk=pk)
       serializer = ProductSerializer(product, context={'request': request})
       return Response(serializer.data)
   
   if request.method == 'PUT':
       product = Product.objects.get(pk=pk)
       serializer = ProductSerializer(product, data=request.data, partial=True)
       if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
       else:
         return Response(serializer.errors)
   
   if request.method == 'DELETE':
       product = Product.objects.get(pk=pk)
       serializer = ProductSerializer(product)
       product.delete()
       return Response(serializer.data)