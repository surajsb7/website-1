# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, an open source suite of business apps
# This module copyright (C) 2015 bloopark systems (<http://bloopark.de>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models


class IrUiView(models.Model):

    _inherit = 'ir.ui.view'

    def render(self, cr, uid, id_or_xml_id, values=None, engine='ir.qweb',
               context=None):
        if not values:
            values = {}

        website_externjs = self.pool.get('website.extern.javascript')

        js_ids = website_externjs.search(
            cr, uid, [('activated', '=', True)], context=context)

        values['javascripts'] = website_externjs.browse(cr, uid, js_ids,
                                                        context=context)

        return super(IrUiView, self).render(cr, uid, id_or_xml_id, values,
                                            engine, context)
