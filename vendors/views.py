from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Vendor
from .serializers import VendorSerializer

User = get_user_model()

class VendorRegisterView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        if user.is_vendor:
            business_name = request.data.get("business_name")
            if not business_name:
                return Response({"error": "Business name is required"}, status=status.HTTP_400_BAD_REQUEST)

            vendor = Vendor.objects.create(user=user, business_name=business_name)
            serializer = VendorSerializer(vendor)
            return Response({"message": "Vendor registered successfully", "vendor": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "You are not a vendor"}, status=status.HTTP_400_BAD_REQUEST)


class VendorProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            vendor = Vendor.objects.get(user=request.user)
            serializer = VendorSerializer(vendor)
            return Response(serializer.data)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor profile not found"}, status=status.HTTP_404_NOT_FOUND)
