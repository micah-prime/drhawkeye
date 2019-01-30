# -*- coding: utf-8 -*-
import os

__author__ = """Micah Sandusky"""
__email__ = 'micah.sandusky@ars.usda.gov'
__version__ = '0.1.0'

__core_config__ = os.path.abspath(os.path.dirname(__file__) + '/CoreConfig.ini')
__recipes__ = os.path.abspath(os.path.dirname(__file__) + '/recipes.ini')


from . import health_check
from . import framework 
