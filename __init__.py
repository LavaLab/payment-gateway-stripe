# -*- coding: utf-8 -*-
"""
    payment-gateway-stripe

    :copyright: (c) The file COPYRIGHT at the top level of this
    :repository contains the full copyright notices.
    :license: , see LICENSE for more details.
"""
from trytond.pool import Pool

def register():
    Pool.register(
        module='payment_gateway_stripe', type_='model'
    )
