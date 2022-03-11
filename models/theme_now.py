from odoo import models


class ThemeNow(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_now_post_copy(self, mod):
        self.enable_view('theme_now.template_header_now')
