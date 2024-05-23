import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from interview.inventory.models import Inventory
from interview.inventory.schemas import InventoryMetaData
from decimal import Decimal


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_inventory_items(inventory_language, inventory_type):
    def _create_inventory_items():
        now = timezone.now()
        metadata = InventoryMetaData(
            description="Test metadata",
            year=2021,
            actors=["Actor 1", "Actor 2"],
            imdb_rating=Decimal('7.5'),
            rotten_tomatoes_rating=85
        ).dict()
        Inventory.objects.create(
            name="Item 1",
            metadata=metadata,
            language=inventory_language,
            type=inventory_type
        )
        Inventory.objects.create(
            name="Item 2",
            metadata=metadata,
            language=inventory_language,
            type=inventory_type
        )
        Inventory.objects.create(
            name="Item 3",
            metadata=metadata,
            language=inventory_language,
            type=inventory_type
        )

    return _create_inventory_items


@pytest.mark.django_db
def test_get_inventory_items_after_date(api_client, create_inventory_items):
    create_inventory_items()
    url = reverse('inventory-list')
    date_after = (timezone.now() + timezone.timedelta(days=7)).date().isoformat()

    response = api_client.get(url, {'date_after': date_after})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0


@pytest.mark.django_db
def test_get_inventory_items_invalid_date(api_client):
    url = reverse('inventory-list')

    response = api_client.get(url, {'date_after': 'invalid-date'})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'Invalid date format' in response.data['error']
