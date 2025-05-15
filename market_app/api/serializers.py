from rest_framework import serializers
from market_app.models import Market, Seller, Product




class MarketSerializer(serializers.ModelSerializer):       
    class Meta: 
         model = Market   
         fields = ['id', 'name', 'location', 'description', 'net_worth']
    
    def validate_no_x_y( value):
        errors = []

        if 'X' in value:
            errors.append('no X in location')
        if 'Y' in value:
             errors.append('no Y in location')

        if errors:
             raise serializers.ValidationError(errors)
        return value


class SellerSerializer(serializers.ModelSerializer):  
     markets = MarketSerializer(many=True, read_only=True)
     market_ids = serializers.PrimaryKeyRelatedField(
          queryset= Market.objects.all(),
          many=True,
          write_only= True,
          source= 'markets'
     ) 

     class Meta:
          model = Seller
          exclude = []
  


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