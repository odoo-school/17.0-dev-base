import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    ods_book_ids = fields.Many2many(
        comodel_name='odoo.school.library.book',
        string='Authors Books',
    )
