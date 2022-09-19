def processing_fee(item_price: float) -> float:
    # charge a 5% processing fee
    marketplace_fee = 0.05
    return item_price * marketplace_fee

def total_cost(item_price: float) -> float:
    return item_price + processing_fee(item_price)