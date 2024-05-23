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
    return Inventory.objects.create(name="Test Inventory", metadata=metadata, language=inventory_language,
                                    type=inventory_type)


@pytest.fixture
def order_tag():
    return OrderTag.objects.create(name="Test Tag")


@pytest.fixture
def create_orders(inventory, order_tag):
    def _create_orders():
        now = timezone.now().date()
        order1 = Order.objects.create(
            inventory=inventory,
            start_date=now - timezone.timedelta(days=10),
            embargo_date=now + timezone.timedelta(days=10),
            is_active=True
        )
        order1.tags.add(order_tag)

        order2 = Order.objects.create(
            inventory=inventory,
            start_date=now - timezone.timedelta(days=5),
            embargo_date=now + timezone.timedelta(days=5),
            is_active=True
        )
        order2.tags.add(order_tag)

        order3 = Order.objects.create(
            inventory=inventory,
            start_date=now - timezone.timedelta(days=20),
            embargo_date=now - timezone.timedelta(days=10),
            is_active=True
        )
        order3.tags.add(order_tag)

    return _create_orders
