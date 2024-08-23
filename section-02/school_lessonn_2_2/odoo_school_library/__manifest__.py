{
    'name': 'Odoo School Library',
    'summary': '',
    'author': 'Odoo School',
    'website': 'https://odoo.school/',
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.2.2.0',

    'depends': [
        'base',
    ],

    'external_dependencies': {
        'python': [],
    },

    'data': [

        'security/ir.model.access.csv',

        'views/odoo_school_library_menu.xml',
        'views/odoo_school_library_book_views.xml',
    ],
    'demo': [
        'demo/res_partner_demo.xml',
        'demo/odoo.school.library.book.csv',
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png'
    ],

}
