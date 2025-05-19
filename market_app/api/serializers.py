from rest_framework import serializers
from market_app.models import Market, Seller, Product




class MarketSerializer(serializers.ModelSerializer):   

#     sellers = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='seller_single')
    sellers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta: 
         model = Market   
         exclude = []
    
    def validate_no_x_y( value):
        errors = []

        if 'X' in value:
            errors.append('no X in location')
        if 'Y' in value:
             errors.append('no Y in location')

        if errors:
             raise serializers.ValidationError(errors)
        return value
    

class MarketHyperlinkedSerializer(MarketSerializer, serializers.HyperlinkedModelSerializer):   
    
     def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

     class Meta: 
         model = Market   
         fields = ['id', 'url', 'name',  'description','location',]
    


class SellerSerializer(serializers.ModelSerializer):  
     markets = MarketSerializer(many=True, read_only=True)
     market_ids = serializers.PrimaryKeyRelatedField(
          queryset= Market.objects.all(),
          many=True,
          write_only= True,
          source= 'markets'
     ) 

     market_count = serializers.SerializerMethodField()

     class Meta:
          model = Seller
          fields = ["id", "name", "market_count", "market_ids", "contact_info", "markets"]
    
     def get_market_count(self, obj):
          return obj.markets.count()
    
  
class SellerListSerializer(SellerSerializer, serializers.HyperlinkedModelSerializer):
         class Meta:
          model = Seller
          fields =  ["url", "name", "market_count", "market_ids", "contact_info"]

class ProductSerializer(serializers.ModelSerializer):  
     markets = MarketSerializer(many=True, read_only=True)
     seller = SellerSerializer(many=True, read_only=True)
     market_ids = serializers.PrimaryKeyRelatedField(
          queryset= Market.objects.all(),
          many=True,
          write_only= True,
          source= 'markets'
     )
     seller_ids = serializers.PrimaryKeyRelatedField(
          queryset= Seller.objects.all(),
          many=True,
          write_only= True,
          source= 'seller'
     ) 

     class Meta:
          model = Product
          exclude = []


class ProductHyperlinkSerializer(ProductSerializer, serializers.HyperlinkedModelSerializer):
     def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

     class Meta: 
         model = Product   
         fields = ['id','name', 'description', 'price']
