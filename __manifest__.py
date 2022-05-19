{
    'name': 'NOW theme',
    'description': 'NOW Theme',
    'category': 'Theme/Services',
    'version': '15.1.20',

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",
    
    'depends': ['theme_common', 'website', 'website_sale'],
    'data': [
        'data/ir_asset.xml',
        'views/customizations.xml',
        'views/website_templates.xml',
        'views/portal_templates.xml',
        'views/snippets/snippets.xml',
        'views/snippets/s_text_block.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_video_169.xml',
        'views/snippets/s_video_43.xml',
    ],
    'images': [
    ],
    'snippet_lists': {
        'homepage': ['s_cover', 's_title', 's_text_block', ],
    },
    'license': 'LGPL-3',
    'assets': {
        'web.assets_qweb': [
            'theme_now/static/src/xml/editor.xml',
        ],        
        'website.assets_editor': [
            'theme_now/static/src/js/tour.js',
        ],
        'web.assets_frontend': [
            'theme_now/static/src/css/custom.css',
            'theme_now/static/lib/mdi/css/materialdesignicons.min.css',
        ],
        'website.assets_wysiwyg': [
            'theme_now/static/src/js/snippets.editor.js',
        ],
    }
}
