import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_deactivate_order(api_client, order):
    url = reverse('deactivate-order', args=[order.id])
    response = api_client.post(url)

    assert response.status_code == status.HTTP_200_OK
    order.refresh_from_db()
    assert not order.is_active
