def calculate_tax(price: float, tax: float, discount: float=0) -> float:
    """Функция вычисляет стоимость товара с учётом налога."""
    if price <= 0:
        raise ValueError('Неверная цена')
    elif tax < 0:
        raise ValueError('Неверный налоговый процент')
    elif tax == 100:
        raise ValueError('Неверный налоговый процент')
    price_with_tax= ((price*tax)/100) + price
    return float(round(price_with_tax-(price*discount), 2))

