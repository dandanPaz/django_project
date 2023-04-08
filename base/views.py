from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework import serializers
from .models import Product,Customers
from rest_framework.response import Response
from .Serializer import ProductSerializer,CustomerSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User



def index(req):
    return JsonResponse('hello', safe=False)

# def login_page(request):
#     context = {
#         'title': 'My Page Title',
#         'message': 'Welcome to my page!'
#     }
#     return render(request, 'login.html', context)

# def Customers_page(request):
#     context = {
#         'title': 'My Page Title',
#         'message': 'Welcome to my page!'
#     }
#     return render(request, 'Customers.html', context)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        # ...
 
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")


@api_view(['GET','POST','DELETE','PUT','PATCH'])
def products(request,id=-1):
    if request.method =='GET':
        if id > -1:
            try:
                temp_prod=Product.objects.get(id=id)
                return Response (ProductSerializer(temp_prod,many=False).data)
            except Product.DoesNotExist:
                return Response ("not found")
        all_prod=ProductSerializer(Product.objects.all(),many=True).data
        return Response (all_prod)
        
    if request.method =='POST':
        prd_serializer=ProductSerializer(data=request.data)
        if prd_serializer.is_valid():
            prd_serializer.save()
            return Response ("post....")
        else:
            return Response (ProductSerializer.errors)
    if request.method =='DELETE':
        try:
            temp_prod= Product.objects.get(id=id)
        except  Product.DoesNotExist:
            return Response ("not found")    
       
        temp_prod.delete()
        return Response ("del...")
    if request.method =='PUT':
        try:
            temp_prod=Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response ("not found")
       
        ser = ProductSerializer(data=request.data)
        old_prod = Product.objects.get(id=id)
        res = ser.update(old_prod, request.data)
        return Response(res)
    


# @api_view(['GET','POST','DELETE','PUT','PATCH'])
# def Customer(request,id=-1):
#     if request.method =='GET':
#         if id > -1:
#             try:
#                 temp_cus=Customers.objects.get(id=id)
#                 return Response (CustomerSerializer(temp_cus,many=False).data)
#             except Customers.DoesNotExist:
#                 return Response ("not found")
#         all_cus=CustomerSerializer(Customers.objects.all(),many=True).data
#         return Response (all_cus)
        
#     if request.method =='POST':
#         cus_serializer=CustomerSerializer(data=request.data)
#         if cus_serializer.is_valid():
#             cus_serializer.save()
#             return Response ("post....")
#         else:
#             print(cus_serializer)
#             return Response (CustomerSerializer.errors)
#     if request.method =='DELETE':
#         try:
#             temp_cus= Customers.objects.get(id=id)
#         except  Customers.DoesNotExist:
#             return Response ("not found")    
       
#         temp_cus.delete()
#         return Response ("del...")
#     if request.method =='PUT':
#         try:
#             temp_cus=Customers.objects.get(id=id)
#         except Customers.DoesNotExist:
#             return Response ("not found")
       
#         ser = CustomerSerializer(data=request.data)
#         old_cus = Customers.objects.get(id=id)
#         res = ser.update(old_cus, request.data)
#         return Response(res)

@permission_classes([IsAuthenticated])
class Customer(APIView):
    def get(self, request, id=-1):  # axios.get
        if int(id) > -1:
            my_model = Customers.objects.get(id=id)
            serializer = CustomerSerializer(my_model, many=False)
        else:
            my_model = Customers.objects.all()
            serializer =CustomerSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):  # axios.post
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):  # axios.put
        my_model = Customers.objects.get(id=id)
        serializer = CustomerSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):  # axios.delete
        my_model = Customers.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   