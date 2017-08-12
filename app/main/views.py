# -*- coding: utf-8 -*-
from app.main import main


@main.route('/', methods=['GET', 'POST'])
def query():
    return "HelloWorld"


@main.route('/hello', methods=['GET'])
def index():
    return "HelloWorld"
