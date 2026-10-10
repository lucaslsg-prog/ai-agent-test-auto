def calculate_discount(amount: float, discount_percentage: float) -> float:
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    if not 0 <= discount_percentage <= 100:
        raise ValueError(
            "Discount percentage must be between 0 and 100."
        )

    discount = amount * (discount_percentage / 100)
    return round(amount - discount, 2)