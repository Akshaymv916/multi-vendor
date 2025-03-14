from rest_framework import generics, permissions, status, serializers
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsVendor

class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not hasattr(self.request.user, 'vendor'):
            raise serializers.ValidationError({"error": "Only vendors can view products"})  
        return Product.objects.filter(vendor=user.vendor)


    def perform_create(self, serializer):
        if not hasattr(self.request.user, 'vendor'):
            raise serializers.ValidationError({"error": "Only vendors can add products"})  
        serializer.save(vendor=self.request.user.vendor)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsVendor]

    def get_queryset(self):
        return Product.objects.filter(vendor=self.request.user.vendor)
