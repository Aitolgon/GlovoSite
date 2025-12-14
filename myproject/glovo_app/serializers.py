from django.contrib.auth import authenticate
from .models import (UserProfile,Category,Store,Contact,Address,StoreMenu,
                     Product,Order,CourierProduct,Review)
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class UserProfileRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name',
                  'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class UserProfileLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','first_name']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name']

class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

class StoreListSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y')
    get_avg_rating = serializers.SerializerMethodField()
    get_avg_procent = serializers. SerializerMethodField()
    get_count_people = serializers. SerializerMethodField()

    class Meta:
        model = Store
        fields = ['id', 'store_name', 'store_image', 'created_date', 'get_avg_rating',
                  'get_avg_procent', 'get_count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_avg_procent(self, obj):
        return obj.get_avg_procent()

    def get_count_people(selfs, obj):
        return obj.get_count_people()


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_stores = StoreListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'category_stores']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['contact_name', "contact_number"]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address_name']


class StoreMenuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreMenu
        fields = ['id', 'menu_name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_image', 'product_description', 'price']


class StoreMenuDetailSerializer(serializers.ModelSerializer):
    product_stores = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = StoreMenu
        fields = ['id', 'menu_name', 'product_stores']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderStatusSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    client = UserProfileNameSerializer

    class Meta:
        model = Order
        fields = ['id', 'product', 'client', 'status']


class CourierProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierProduct
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    client = UserProfileDetailSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Review
        fields = ['client', 'text', 'courier', 'created_date', 'rating']


class StoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class StoreDetailSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y')
    category = CategoryNameSerializer()
    owner = UserProfileNameSerializer()
    contact_stores = ContactSerializer(many=True, read_only=True)
    address_stores = AddressSerializer(many=True, read_only=True)
    menu_stores = StoreMenuDetailSerializer(many=True, read_only=True)
    store_reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Store
        fields = ['id', 'store_name', 'store_image', 'category', 'created_date',
                  'description', 'owner', 'contact_stores', 'address_stores',
                  'menu_stores', 'store_reviews']

