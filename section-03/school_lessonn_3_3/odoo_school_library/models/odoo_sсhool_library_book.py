import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)

CONST_EXP = "Odoo school constant example"


class OSLBook(models.Model):
    _name = 'odoo.school.library.book'
    _description = 'Book'

    name = fields.Char(
        size=64,
        translate=True,
        copy=False,
    )

    active = fields.Boolean(
        default=True,
        groups='base.group_system',
    )
    description = fields.Text(
        string='Book Description',
        index=True,
        translate=True,
    )
    html_note = fields.Html()
    release_date = fields.Date(default=fields.Date.today(), )
    # release_datetime = fields.Datetime(default=lambda self: fields.Datetime.now(), )
    author_names = fields.Char(
        default=lambda self: self._default_all_authors_get(), )

    company_id = fields.Many2one(
        comodel_name='res.company',
        required=True,
        readonly=True,
        default=lambda self: self.env.company,
    )
    company_currency_id = fields.Many2one(
        comodel_name="res.currency",
        string='Currency',
        related='company_id.currency_id',
        readonly=True,
        tracking=True,
    )
    # price = fields.Float(string='Price', digits=(16, 1), )
    monetary_price = fields.Monetary(
        string='Price Monetary',
        currency_field='company_currency_id',
    )
    inventory_state = fields.Selection(
        [('available', 'Available'),
         ('pending', 'Pending'),
         ('out_of_stock', 'Out of stock')],
        default="out_of_stock",
        string='Inventory State',
    )
    res_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Main Author",
        index=True,
        help="Main Author who created this book",
    )
    partner_country_name = fields.Char(
        related='res_partner_id.country_id.name'
    )
    res_partner_ids = fields.Many2many(
        comodel_name='res.partner',
        string="Additional Authors",
        help="Additional Authors who took part in creating this book",
    )
    # book_cover_image = fields.Binary(
    #     attachment=False,
    # )
    book_cover_image = fields.Image(
        max_width=512,
        max_height=512,
    )

    def _default_all_authors_get(self):
        author_names = ''
        res_partner_ids = self.res_partner_ids + self.res_partner_id
        for partner_id in res_partner_ids:
            author_names += partner_id.name
        return author_names
