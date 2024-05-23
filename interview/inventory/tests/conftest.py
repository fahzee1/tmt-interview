import pytest
from interview.inventory.models import InventoryLanguage, InventoryType, InventoryTag


@pytest.fixture
def inventory_language():
    return InventoryLanguage.objects.create(name="English")


@pytest.fixture
def inventory_type():
    return InventoryType.objects.create(name="Book")


@pytest.fixture
def inventory_tag():
    return InventoryTag.objects.create(name="Fiction")
