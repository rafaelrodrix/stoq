# -*- coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## Copyright (C) 2007 Async Open Source <http://www.async.com.br>
## All rights reserved
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., or visit: http://www.gnu.org/.
##
##  Author(s):  Fabio Morbec              <fabio@async.com.br>
##  Author(s):  George Y. Kussumoto       <george@async.com.br>
##
##
""" Payment receival report implementation """

from decimal import Decimal

from stoqlib.reporting.base.tables import ObjectTableColumn as OTC
from stoqlib.reporting.template import BaseStoqReport, ObjectListReport
from stoqlib.lib.translation import stoqlib_gettext as _
from stoqlib.lib.validators import get_formatted_price

class _BasePaymentReport(ObjectListReport):
    """Base report for Payable and Receivable reports"""
    report_name = _("Payment Report")
    main_object_name = "payments"

    def __init__(self, filename, payments, *args, **kwargs):
        self._payments = payments
        ObjectListReport.__init__(self, filename, payments,
                                  _BasePaymentReport.report_name,
                                  landscape=True, *args, **kwargs)
        self._setup_table()

    def _setup_table(self):
        total_value = sum([item.value for item in self._payments],
                          Decimal(0))
        self.add_summary_by_column(_(u'Value'),
                                   get_formatted_price(total_value))
        self.add_object_table(self._payments, self.get_columns(),
                              summary_row=self.get_summary_row())


class ReceivablePaymentReport(_BasePaymentReport):
    """
    This report shows a list of receivable payments. For each payment it shows:
    payment number, description, drawee, due date, paid date, status and value.
    """


class PayablePaymentReport(_BasePaymentReport):
    """
    This report shows a list of payable payments. For each payment it shows:
    payment number, description, supplier, due date, paid date,
    status and value.
    """


class BillCheckPaymentReport(_BasePaymentReport):
    """This report shows a list of payments and some information about the
    bill or check method payment (if available) like: the bank id, the bank
    branch, the bank account. The field payment_number in the report can be
    the check number or the bill number.
    """


class PaymentFlowHistoryReport(BaseStoqReport):
    report_name = _(u'Payment Flow History')

    def __init__(self, filename, payment_histories, *args, **kwargs):
        self._payment_histories = payment_histories
        BaseStoqReport.__init__(self, filename,
                                PaymentFlowHistoryReport.report_name,
                                landscape=True, *args, **kwargs)
        self._setup_payment_histories_table()

    def _setup_payment_histories_table(self):
        for payment_history in self._payment_histories:
            history_date = payment_history.history_date.strftime('%x')
            self.add_paragraph(_(u'Day: %s' % history_date), style='Title')
            self._add_history_table(payment_history)

    def _add_history_table(self, history):
        self.add_object_table([history], self._get_payment_history_columns())
        if (history.to_receive != history.to_pay or
            history.received != history.paid):
            payments = list(history.get_divergent_payments())
            if payments:
                self.add_object_table(payments, self._get_payment_columns())
        self.add_blank_space(10)

    def _get_payment_history_columns(self):
        return [
            OTC(_(u'Last Balance'), lambda obj:
                '%s' % get_formatted_price(obj.get_last_day_real_balance())),
            OTC(_(u'To Receive'), lambda obj:
                    '%s' % get_formatted_price(obj.to_receive)),
            OTC(_(u'To Pay'), lambda obj:
                    '%s' % get_formatted_price(obj.to_pay)),
            OTC(_(u'Received'), lambda obj:
                    '%s' % get_formatted_price(obj.received)),
            OTC(_(u'Paid'), lambda obj: '%s' % get_formatted_price(obj.paid)),
            OTC(_(u'Balance Expected'), lambda obj:
                    '%s' % get_formatted_price(obj.balance_expected)),
            OTC(_(u'Balance Real'), lambda obj:
                    '%s' % get_formatted_price(obj.balance_real)),]

    def _get_payment_columns(self):
        return [
            OTC(_(u'Description'), lambda obj: '%s' % obj.description),
            OTC(_(u'Value'), lambda obj:
                                '%s' % get_formatted_price(obj.value)),
            OTC(_(u'Paid Value'), lambda obj:
                    '%s' % get_formatted_price(obj.paid_value or Decimal(0))),
            OTC(_(u'Due Date'), lambda obj: '%s' % obj.due_date.strftime('%x')),
            OTC(_(u'Paid Date'), lambda obj: '%s' % obj.get_paid_date_string()),
        ]

    def get_title(self):
        return self.report_name
