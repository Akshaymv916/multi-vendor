from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail
from .models import Order
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer, OrderCreateSerializer, OrderStatusUpdateSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        order = serializer.save()  
        
        user_email = self.request.user.email
        
        subject = "Order Confirmation"
        message = f"Dear {self.request.user.email},\n\n"
        message += f"Thank you for your order! Your order ID is {order.id}.\n"
        message += f"Total Amount: ₹{order.total_amount}\n"
        message += "Your order will be processed soon.\n\n"
        message += "Best regards,\nYour Shop Team"

        # Send Email
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,  #
            [user_email],
            fail_silently=False,
        )

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(customer=self.request.user)

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(customer=self.request.user)

class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(customer=self.request.user)
    
class OrderStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
            
           
            if not request.user.is_staff:
                return Response({"error": "Permission denied. Only admins can update order status."}, status=status.HTTP_403_FORBIDDEN)

            serializer = OrderStatusUpdateSerializer(order, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                
                # Send email notification
                self.send_status_update_email(order)
                
                return Response({"message": "Order status updated successfully", "order": serializer.data}, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

    def send_status_update_email(self, order):
        """Send an email notification when the order status changes."""
        subject = f"Order #{order.id} Status Update"
        message = f"Dear {order.customer.email},\n\n"
        message += f"Your order status has been updated to: **{order.status.upper()}**.\n"
        message += f"Total Amount: ₹{order.total_amount}\n\n"
        message += "Thank you for shopping with us!\nBest regards,\nYour Shop Team"

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [order.customer.email], 
            fail_silently=False,
        )
