from .models import Order
from .serializers import OrderSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
import sys
sys.path.append("..")
from permissions.permissions import AuthorOrReadOnly
from django.contrib.auth.models import User


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    permission_classes = [permissions.IsAuthenticated, AuthorOrReadOnly]

    # lookup_field = 'author'0
 
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
