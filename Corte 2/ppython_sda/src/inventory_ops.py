"""Operaciones de inventario basadas en una lista de diccionarios.

Cada producto es un diccionario con las llaves:
- id (int)
- nombre (str)
- precio (float)
- cantidad (int)

Se busca mantener operaciones simples para comparar su costo.

Complejidad esperada (n = número de productos):
- add_product: O(1) amortizado (calcula id en O(1) si llevamos un contador externo, aquí usamos max -> O(n)).
- find_by_id: O(n) en lista; con dict sería O(1) promedio.
- update_stock: O(n) por la búsqueda.
- remove_product: O(n) por búsqueda y potencial desplazamiento.
- total_value: O(n) porque debe recorrer todos los productos.

Nota: Se mantiene una implementación intencionalmente basada en lista para contrastar con un dict.
"""
from __future__ import annotations
from typing import List, Dict, Optional

Producto = Dict[str, object]

__all__ = [
    "add_product",
    "find_by_id",
    "update_stock",
    "remove_product",
    "total_value",
]

def _next_id(inventario: List[Producto]) -> int:
    """Obtiene el siguiente id. O(n) por usar max.
    (Se deja así a propósito para análisis; podría optimizarse guardando un contador)."""
    if not inventario:
        return 0
    return max(p["id"] for p in inventario if "id" in p) + 1


def add_product(inventario: List[Producto], nombre: str, precio: float, cantidad: int) -> Producto:
    """Agrega un nuevo producto y retorna el diccionario creado.
    Validaciones básicas y asignación de id incremental.
    O(n) por _next_id.
    """
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa")
    product_id = _next_id(inventario)
    producto: Producto = {
        "id": product_id,
        "nombre": nombre,
        "precio": float(precio),
        "cantidad": int(cantidad),
    }
    inventario.append(producto)
    return producto


def find_by_id(inventario: List[Producto], product_id: int) -> Optional[Producto]:
    """Busca secuencialmente un producto. O(n)."""
    for producto in inventario:
        if producto.get("id") == product_id:
            return producto
    return None


def update_stock(inventario: List[Producto], product_id: int, nueva_cantidad: int) -> bool:
    """Actualiza la cantidad de un producto. O(n). Retorna True si se modificó."""
    if nueva_cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa")
    producto = find_by_id(inventario, product_id)
    if producto is None:
        return False
    producto["cantidad"] = nueva_cantidad
    return True


def remove_product(inventario: List[Producto], product_id: int) -> bool:
    """Elimina el producto con id dado. O(n)."""
    for i, producto in enumerate(inventario):
        if producto.get("id") == product_id:
            del inventario[i]
            return True
    return False


def total_value(inventario: List[Producto]) -> float:
    """Suma precio * cantidad. O(n)."""
    total = 0.0
    for producto in inventario:
        try:
            total += float(producto.get("precio", 0)) * int(producto.get("cantidad", 0))
        except (TypeError, ValueError):
            # Si hay datos corruptos, se ignoran (diseño defensivo)
            continue
    return total

if __name__ == "__main__":  # Pequeña demostración manual
    inv: List[Producto] = []
    add_product(inv, "Teclado", 50_000, 10)
    add_product(inv, "Mouse", 25_000, 5)
    print("Inventario:", inv)
    print("Total:", total_value(inv))
