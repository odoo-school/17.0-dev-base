import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_ods_author = fields.Boolean()
    ods_book_ids = fields.One2many(
        comodel_name='odoo.school.library.book',
        inverse_name='res_partner_id',
        string='Authors Books',
    )
    ods_books_count = fields.Integer(
        compute='_compute_ods_books_count',
        store=True,
    )

    @api.depends('ods_book_ids')
    def _compute_ods_books_count(self):
        for partner in self:
            partner.ods_books_count = len(partner.ods_book_ids)
