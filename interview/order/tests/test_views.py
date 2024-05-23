import pytest
from django.urls import reverse
from rest_framework import status
from django.utils import timezone


@pytest.mark.django_db
def test_list_orders_by_date(api_client, create_orders):
    create_orders()
    url = reverse('list-orders-by-date')
    start_date = (timezone.now().date() - timezone.timedelta(days=15)).isoformat()
    embargo_date = (timezone.now().date() + timezone.timedelta(days=7)).isoformat()

    response = api_client.get(url, {'start_date': start_date, 'embargo_date': embargo_date})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_list_orders_by_date_invalid_date(api_client, create_orders):
    create_orders()
    url = reverse('list-orders-by-date')

    response = api_client.get(url, {'start_date': 'invalid-date', 'embargo_date': 'invalid-date'})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'error' in response.data
    assert response.data['error'] == 'Invalid or missing date format. Use YYYY-MM-DD.'
