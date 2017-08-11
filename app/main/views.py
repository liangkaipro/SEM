#coding: utf-8
from flask import render_template,current_app,redirect,\
    url_for,flash
from .forms import QueryForm
from ..models import Stuinfo
from . import main

@main.route('/'，methods=['GET','POST'])
def query():
   form = QueryForm()

