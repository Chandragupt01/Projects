from rest_framework import serializers
from ..models import Carlist,Showroomlist,Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'

# validators
def alphanumeric(value):
    if not str(value).isalnum():
        raise serializers.ValidationError("only alpha numeric characters are allowed")

class CarSerializer(serializers.ModelSerializer):
    # -------------------------------------this code is for default serializerclass ie serializers.Serializer-----------------------------------------------------
    # id =serializers.IntegerField(read_only=True)
    # name=serializers.CharField()
    # description=serializers.CharField()
    # active=serializers.BooleanField(read_only=True)
    # chassisNumber=serializers.CharField(validators=[alphanumeric])
    # price=serializers.DecimalField(max_digits=9,decimal_places=2)

    # def create(self,validated_data):
    #     return Carlist.objects.create(**validated_data)
    
    # def update(self,instance,validated_data):
    #     instance.name=validated_data.get('name',instance.name)
    #     instance.description=validated_data.get('description',instance.description)
    #     instance.active=validated_data.get('active',instance.active)
    #     instance.chassisNumber=validated_data.get('chassisNumber',instance.chassisNumber)
    #     instance.price=validated_data.get('price',instance.price)
    #     instance.save()
    #     return instance

    # -------------------------------------this code is for default serializerclass ie serializers.Serializer-----------------------------------------------------
    discounted_price=serializers.SerializerMethodField()
    Reviews = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model=Carlist
        # fields=['id','name','description']#'__all__'
        fields='__all__'
        # exclude=['name']

    def get_discounted_price(self,object):
        discountprice=object.price-5000
        return discountprice
    # Field level validation 
    def validate_price(self,value):
        if value<=20000.00:
            raise serializers.ValidationError("Price must be greater than 20000.00")
        return value
    
    # object level validation 
    def validate(self,data):
        if data['name']==data['description']:
            raise serializers.ValidationError("Name and Description must be different")
        return data
    

class ShowroomSerializer(serializers.ModelSerializer):
    # Showrooms=CarSerializer(many=True,read_only=True)
    Showrooms=serializers.StringRelatedField(many=True)
    class Meta:
        model=Showroomlist
        fields='__all__'
