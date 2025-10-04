import math
import pytest
from ppython_sda.src.inventory_ops import (
    add_product,
    find_by_id,
    update_stock,
    remove_product,
    total_value,
)

@pytest.fixture
def empty_inventory():
    return []

@pytest.fixture
def sample_inventory(empty_inventory):
    add_product(empty_inventory, "A", 10.0, 2)  # id 0
    add_product(empty_inventory, "B", 5.5, 4)   # id 1
    add_product(empty_inventory, "C", 1.0, 10)  # id 2
    return empty_inventory

# 1. add_product + validaciones
def test_add_product_assigns_incremental_id(sample_inventory):
    ids = [p['id'] for p in sample_inventory]
    assert ids == [0,1,2]

# 2. find_by_id
def test_find_by_id_found(sample_inventory):
    p = find_by_id(sample_inventory, 1)
    assert p is not None and p['nombre'] == 'B'

# 3. update_stock
def test_update_stock_success(sample_inventory):
    ok = update_stock(sample_inventory, 2, 99)
    assert ok is True
    assert find_by_id(sample_inventory, 2)['cantidad'] == 99

# 4. remove_product
def test_remove_product(sample_inventory):
    removed = remove_product(sample_inventory, 1)
    assert removed is True
    assert find_by_id(sample_inventory, 1) is None

# 5. total_value
def test_total_value(sample_inventory):
    # A: 10*2=20, B:5.5*4=22, C:1*10=10 -> 52
    assert math.isclose(total_value(sample_inventory), 52.0)

# Casos límite / errores

def test_add_product_negative_price(empty_inventory):
    with pytest.raises(ValueError):
        add_product(empty_inventory, "X", -1.0, 1)

def test_update_stock_negative(sample_inventory):
    with pytest.raises(ValueError):
        update_stock(sample_inventory, 0, -5)

def test_remove_product_not_found(sample_inventory):
    assert remove_product(sample_inventory, 999) is False

# Degeneración: muchos elementos y búsqueda O(n)

def test_find_by_id_last_element_performance():
    inv = []
    for i in range(2000):
        add_product(inv, f"P{i}", 1.0, 1)
    # Buscar el último (caso peor para búsqueda lineal) -> O(n)
    p = find_by_id(inv, 1999)
    assert p is not None and p['nombre'] == 'P1999'
