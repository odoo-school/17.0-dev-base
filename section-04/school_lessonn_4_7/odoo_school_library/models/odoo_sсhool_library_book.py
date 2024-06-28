import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)

CONST_EXP = "Odoo school constant example"


class OSLBook(models.Model):
    _name = 'odoo.school.library.book'
    _inherit = ['mail.thread']
    _description = 'Book'

    name = fields.Char(
        size=64,
        required=True,
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
    release_date = fields.Date(
        default=fields.Date.today(),
    )
    author_names = fields.Char(
        default=lambda self: self._default_all_authors_get(),
    )
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
        domain=[('is_ods_author', '=', True)],
        ondelete='set null',
    )
    partner_country_name = fields.Char(
        related='res_partner_id.country_id.name'
    )
    res_partner_ids = fields.Many2many(
        comodel_name='res.partner',
        string="Additional Authors",
        help="Additional Authors who took part in creating this book",
        readonly=False,
        relation="osl_book_res_partner_rel",
        column1="ods_book_id",
        column2="res_partner_id",
    )
    res_partner_readers_ids = fields.Many2many(
        comodel_name='res.partner',
        string="Book readers",
        help="At this moment they are reading the book",
        readonly=True,
        relation="osl_book_res_partner_reader_rel",
        column1="ods_book_id",
        column2="res_partner_id",
    )
    book_cover_image = fields.Image(
        max_width=512,
        max_height=512,
    )
    res_partner_count = fields.Integer(
        compute='_compute_count',
    )
    # for booking calendar
    start_booking_date = fields.Date(
        default=fields.Date.today(),
        required=True,
    )
    end_booking_date = fields.Date(
        default=fields.Date.today(),
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The book name must be unique!')
    ]

    def _default_all_authors_get(self):
        author_names = ''
        res_partner_ids = self.res_partner_ids + self.res_partner_id
        for partner_id in res_partner_ids:
            author_names += partner_id.name
        return author_names

    @api.depends('res_partner_ids')
    def _compute_count(self):
        for obj in self:
            obj.res_partner_count = len(obj.res_partner_ids.ids) + len(obj.res_partner_id.ids)

    def show_to_author(self):
        self.ensure_one()
        self.res_partner_id

        _logger.info(self.ids)
        _logger.info(self.res_partner_ids.ids)
        _logger.info(f"Book price = {self._context.get('book_price')}")
        pass
