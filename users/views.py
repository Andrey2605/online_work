from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from users.models import Payments
from users.serializers import PaymentsSerializer


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [OrderingFilter]
    filterset_fields = ('payment_method',)
    ordering_fields = ['payment_date',]


