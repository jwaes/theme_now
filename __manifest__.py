{
    'name': 'NOW theme',
    'description': 'NOW Theme',
    'category': 'Theme/Services',
    'version': '1.70',

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",
    
    'depends': ['theme_common', 'website', 'website_blog'],
    'data': [
        'data/data.xml',
        'data/ir_asset.xml',
        'data/product_snippet_template_data.xml',
        'views/customizations.xml',
        'views/website_sale.xml',
        'views/website_templates.xml',
        'views/portal_templates.xml',
        'views/website_blog_posts_loop.xml',
        'views/website_blog_templates.xml',
        'views/snippets/snippets.xml',
        'views/snippets/s_text_block.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_video_169.xml',
        'views/snippets/s_video_43.xml',
        # 'views/snippets/s_video_yt.xml',
        # 'views/snippets/s_video_plyr.xml',
    ],
    'images': [
    ],
    'snippet_lists': {
        'homepage': ['s_cover', 's_title', 's_text_block', 's_video_plyr',],
    },
    'license': 'LGPL-3',
    'assets': {     
        'website.assets_editor': [
            'theme_now/static/src/js/tour.js',
        ],
        'web.assets_frontend': [
            'theme_now/static/src/css/custom.css',
            'theme_now/static/src/css/cust.scss',
            'theme_now/static/lib/fontsdotcom/css/fonts.css',
            'theme_now/static/lib/fontsdotcom/js/fonts.js',            
            'theme_now/static/lib/mdi/css/materialdesignicons.min.css',
            'theme_now/static/src/js/website_sale.js',
        ],
        # 'website.assets_wysiwyg': [
        #     # 'theme_now/static/src/js/snippets.editor.js',
        #     # 'theme_now/static/src/snippets/s_video_plyr/options.js',
        # ],
    }
}
