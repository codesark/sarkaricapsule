from django.contrib.admin.sites import AdminSite
from django.utils.translation import ugettext_lazy as _

# --- Admin Site Configuration ----- 
AdminSite.site_title = _('Sarkari Capsule')
AdminSite.site_header = _('Sarkari Capsule Administration')
AdminSite.index_title = _('Site Administration')
#  ----------------- END ----------------------
