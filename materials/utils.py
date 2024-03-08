import stripe
from pprint import pprint
from config.settings import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY


def get_url_for_payment(course):
    response_price = stripe.Price.create(
        currency="usd",
        unit_amount=course.price*100,
        product_data={"name": course.title},
    )
    response_url = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": response_price["id"], "quantity": 1}],
        mode="payment",
    )
    return response_url["url"]