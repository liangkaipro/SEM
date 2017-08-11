#coding: utf-8
from flask import Blueprint


mian = Blueprint('mian',__name__)

from . import views,errors