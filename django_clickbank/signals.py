from django.dispatch import Signal


sale = Signal()

rebill = Signal()

refund = Signal()

chargeback = Signal()

insuffient_funds = Signal()

cancel = Signal()

uncancel = Signal()

test = Signal()
