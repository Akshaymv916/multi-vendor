from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product  # Import Product model

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price_at_purchase']

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.id')
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'total_amount', 'status', 'created_at', 'items']
    
class OrderCreateSerializer(serializers.ModelSerializer):
    items = serializers.ListField(write_only=True)  # Accept a list of items in the request body

    class Meta:
        model = Order
        fields = ['id', 'total_amount', 'status', 'created_at', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])  
        user = self.context['request'].user  
        
        order = Order.objects.create(**validated_data, customer=user)

        total_price = 0

        for item in items_data:
            product = Product.objects.get(id=item['product_id'])
            quantity = item['quantity']

            if product.stock < quantity:
                raise serializers.ValidationError(f"Insufficient stock for {product.name}")

            price_at_purchase = product.price
            total_price += price_at_purchase * quantity

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price_at_purchase=price_at_purchase
            )

            product.stock -= quantity
            product.save()

        order.total_amount = total_price  
        order.save()
        return order
    


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']
    
    def validate_status(self, value):
        if value not in ['pending', 'shipped', 'delivered']:
            raise serializers.ValidationError("Invalid status. Choose from 'pending', 'shipped', or 'delivered'.")
        return value
