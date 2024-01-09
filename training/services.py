import stripe
from django.conf import settings

from config.settings import STRIPE_API_KEY


def create_stripe_session(course, user, amount):
    """Создание сессии оплаты в страйп"""
    stripe.api_key = STRIPE_API_KEY

    # Создание продукта для оплаты в страйп.
    product_for_stripe = stripe.Product.create(name=course.title)

    # Создание цены для оплаты продукта в страйп.
    price_for_stripe = stripe.Price.create(
        product=product_for_stripe.id,
        unit_amount=int(amount * 100),
        currency='usd',
    )

    # Создание сессии оплаты в страйп.
    session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': price_for_stripe.id,
                'quantity': 1,

            },
        ],
        customer_email=user.email,
        mode='payment',
        success_url=f'{settings.DOMAIN_NAME}/payment/',
        cancel_url=f'{settings.DOMAIN_NAME}/payment/',
    )
    return session


def get_stripe_session(stripe_id) -> dict:
    """Получение сессии оплаты в страйп"""
    stripe.api_key = STRIPE_API_KEY
    return stripe.checkout.Session.retrieve(stripe_id)