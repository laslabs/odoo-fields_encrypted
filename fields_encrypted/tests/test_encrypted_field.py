# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc [https://laslabs.com]
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from openerp import models, fields
from openerp.tests.common import TransactionCase


class TestModel(models.Model):
    _name = 'test.model'
    enc_test = fields.EncryptedText()


class TestEncryptedText(TransactionCase):

    ORIG = 'TEST'

    def setUp(self):
        super(TestEncryptedText, self).setUp()
        self.fixture = {
            'enc_test': self.ORIG,
        }
        self.mdl = self.env['test.model']

    # def test_database_create_encrypt(self, ):
    #     """
    #     Verifies encryption method called on create
    #     """
    #     rec = self.mdl.create(self.fixture)
    #     actual = rec.enc_test

    def test_no_error_on_update_or_create(self, ):
        rec = self.mdl.create(self.fixture)
        rec.update({
            'enc_test': 'Derp'
        })

    def test_read_equals_orig(self, ):
        rec = self.mdl.create(self.fixture)
        self.assertEqual(self.ORIG, rec.enc_text)
