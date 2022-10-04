odoo.define('theme_now.cart', function (require) {
    'use strict';
    
    var publicWidget = require('web.public.widget');

    publicWidget.registry.websiteSaleCartLink.prototype.selector += ', #icons_menu a[href$="/shop/cart"]';


});