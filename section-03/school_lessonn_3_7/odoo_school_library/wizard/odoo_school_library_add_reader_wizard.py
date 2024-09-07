import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class OSLAddReader(models.TransientModel):
    _name = 'odoo.school.library.add.reader.wizard'
    _description = 'Add Reader to book'

    ods_book_id = fields.Many2one(
        comodel_name='odoo.school.library.book',
        string='Book',
        readonly=True,
    )
    res_partner_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Readers',
    )

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        if self.env.context.get('active_id'):
            book_id = self.env['odoo.school.library.book'].browse(self.env.context.get('active_id'))
            res['ods_book_id'] = book_id.id
            res['res_partner_ids'] = [(6, 0, book_id.res_partner_readers_ids.ids)]
        return res

    def add_reader(self):
        self.ods_book_id.res_partner_readers_ids = self.res_partner_ids
