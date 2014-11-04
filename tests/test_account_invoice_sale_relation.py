#!/usr/bin/env python
#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_depends


class AccountInvoiceSaleRelationTestCase(unittest.TestCase):
    '''
    Test Account Invoice Sale Relation module.
    '''

    def setUp(self):
        module = 'account_invoice_sale_relation'
        trytond.tests.test_tryton.install_module(module)

    def test0006depends(self):
        '''
        Test depends.
        '''
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        AccountInvoiceSaleRelationTestCase))
    return suite