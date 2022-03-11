{
    'name': 'NOW theme',
    'description': 'NOW Theme',
    'category': 'Theme/Services',
    'version': '15.1.17',

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",
    
    'depends': ['theme_common'],
    'data': [
        'data/ir_asset.xml',
        'views/customizations.xml',
        'views/website_templates.xml',
        'views/portal_templates.xml',
        'views/snippets/s_text_block.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_image_text.xml',

    ],
    'images': [
    ],
    'snippet_lists': {
        'homepage': ['s_cover', 's_title', 's_text_block', ],
    },
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_now/static/src/js/tour.js',
        ],
        'web.assets_frontend': [
            'theme_now/static/src/css/custom.css',
            'theme_now/static/lib/mdi/css/materialdesignicons.min.css',
        ],
    }
}
