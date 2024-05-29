import pytest
from django.utils import timezone
from rest_framework.test import APIClient
from interview.inventory.models import Inventory, InventoryLanguage, InventoryType
from interview.order.models import Order, OrderTag
from decimal import Decimal


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def inventory_language():
    return InventoryLanguage.objects.create(name="English")


@pytest.fixture
def inventory_type():
    return InventoryType.objects.create(name="Book")


@pytest.fixture
def inventory(inventory_language, inventory_type):
    metadata = {
        "description": "Test metadata",
        "year": 2021,
        "actors": ["Actor 1", "Actor 2"],
        "imdb_rating": Decimal('7.5'),  # Use Decimal here
        "rotten_tomatoes_rating": 85
    }
    return Inventory.objects.create(name="Test Inventory", metadata=metadata, language=inventory_language, type=inventory_type)


@pytest.fixture
def order_tag():
    return OrderTag.objects.create(name="Test Tag")


@pytest.fixture
def order(inventory, order_tag):
    order = Order.objects.create(
        inventory=inventory,
        start_date=timezone.now().date(),
        embargo_date=timezone.now().date() + timezone.timedelta(days=30),
        is_active=True
    )
    order.tags.add(order_tag)
    return order
