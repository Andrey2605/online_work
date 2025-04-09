import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product():
    return stripe.Product.create(name="Название продукта")


def create_stripe_price(payment_amount, product):
    """Создает цену в страйпе"""

    return stripe.Price.create(
        currency="rub",
        unit_amount=payment_amount,
        product_data={"name": "Payments"},
    )


def create_stripe_session(price):
    """Создает сессию на оплату в страйпе"""

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
