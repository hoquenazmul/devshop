from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    '''
    It's for converting Product model to dict, so we can pass into `render(dict)`
    Product model => Internal Representation of a Product. 
    ProductSerializer => External Representation of Product model. 
    '''
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)