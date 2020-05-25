from django.conf.urls import url
from django.urls import path
from ..core import TOKEN_PATTERN
from . import views

urlpatterns = [
    url(r"^%s/$" % (TOKEN_PATTERN,), views.details, name="details"),
    url(r"^%s/payment/$" % (TOKEN_PATTERN,), views.payment, name="payment"),
    # url(
    #     r"^%s/payment/(?P<gateway>[-\w]+)/$" % (TOKEN_PATTERN,),
    #     views.start_payment,
    #     name="payment",
    # ),

    url(
    r"^%s/payment_success/$" % (TOKEN_PATTERN,),
    views.start_payment,
    name="payment1",
    ),

    # url(r'^payment/(?P<order>[-\w]+)/$', views.start_payment, name="payment"),
    # path("payment/(?P<order>[-\w]+)/", views.start_payment, name="payment1"),
    url(
        r"^%s/cancel-payment/$" % (TOKEN_PATTERN,),
        views.cancel_payment,
        name="cancel-payment",
    ),
    url(
        r"^%s/payment-success/$" % (TOKEN_PATTERN,),
        views.payment_success,
        name="payment-success",
    ),
    url(
        r"^%s/checkout-success/$" % (TOKEN_PATTERN,),
        views.checkout_success,
        name="checkout-success",
    ),
    url(
        r"^%s/attach/$" % (TOKEN_PATTERN,),
        views.connect_order_with_user,
        name="connect-order-with-user",
    ),
]
