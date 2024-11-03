def calculate_tax(price: float, tax: float) -> float:
    """Функция вычисляет стоимость товара с учётом налога."""
    if price <= 0:
        raise ValueError('Неверная цена')
    if tax < 0 or tax == 100:
        raise ValueError('Неверный налоговый процент')
    return float(round((price*tax/100)+price))


print(calculate_tax(60, 13))