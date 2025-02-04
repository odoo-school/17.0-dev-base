{
    'name': 'Odoo School Library',
    'summary': '',
    'author': 'Odoo School',
    'website': 'https://odoo.school/',
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.5.4.0',

    'depends': [
        'base',
        'account',
    ],

    'external_dependencies': {
        'python': [],
    },

    'data': [
        'security/ir.model.access.csv',

        'wizard/odoo_school_library_add_reader_wizard_view.xml',

        'views/odoo_school_library_menu.xml',
        'views/odoo_school_library_book_views.xml',

        'views/res_partner_view.xml',

        'report/odoo_school_library_book_report.xml',
        'report/res_partner_report.xml',
        'data/odoo_school_library_book_cron.xml',
    ],

    'demo': [
        'demo/res_partner_demo.xml',
        'demo/odoo.school.library.book.csv',
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png',
    ],

}
