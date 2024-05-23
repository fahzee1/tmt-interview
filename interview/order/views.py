from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.dateparse import parse_date
from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer
from rest_framework import status


# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class ListOrdersByDateView(APIView):
    def get(self, request, *args, **kwargs):
        start_date_str = request.query_params.get('start_date')
        embargo_date_str = request.query_params.get('embargo_date')

        start_date = parse_date(start_date_str)
        embargo_date = parse_date(embargo_date_str)

        if not start_date or not embargo_date:
            return Response({'error': 'Invalid or missing date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        orders = Order.objects.filter(start_date__gte=start_date, embargo_date__lte=embargo_date)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
