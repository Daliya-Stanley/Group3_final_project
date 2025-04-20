def get_stock_remaining(product_id, purchased):
    return max(0, 5 - purchased.get(str(product_id), 0))

def get_product_cart():
    from flask import session
    return session.setdefault('product_cart', [])

def get_experience_cart():
    from flask import session
    return session.setdefault('experience_cart', [])
