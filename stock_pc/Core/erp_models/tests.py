import os
import sys

sys.path.append('../../')

"""from stock_pc.stock_pc.wsgi import *
from stock_pc.Core.erp_models.models import Type"""


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_pc.settings')

application = get_wsgi_application()

from stock_pc.Core.erp_models.models import Type
