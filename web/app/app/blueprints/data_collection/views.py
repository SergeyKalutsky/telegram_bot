import sys
import os
import shutil
from datetime import datetime
from app.db.db import insert_data, select_data, select_job, insert_job, select_description, delete_data, select_data_type
from app.core.helpers import make_word_doc
from flask import Flask, render_template, request, session,\
    redirect, url_for, jsonify, Blueprint, send_file
from flask_login import login_required
from flask import current_app as app
from flask_principal import Principal, Permission, Identity, RoleNeed, identity_changed, \
    identity_loaded, AnonymousIdentity, UserNeed


data_collection = Blueprint('data_collection', __name__)


@data_collection.route("/delete_entity", methods=['GET', 'POST'])
@login_required
def delete_entity():
    if request.method == 'POST':
        id_ = int(request.form['id'])
        tipe_id = select_data_type(id_)
        if tipe_id == 1:
            jobs = select_job(company_id=id_)
        else:
            jobs = select_job(house_id=id_)
        # delete data from db
        delete_data(id_, tipe_id)
        # remove all assosiated data
        for job_id in jobs:
            shutil.rmtree(f'static/data/{job_id[0]}')
        return jsonify({'msg': 'Данные удалены'})

    companies, houses = select_data(1), select_data(2)
    data = companies + houses
    return render_template('delete_entity.html', data=data)


@data_collection.route("/manage_tasks", methods=['GET', 'POST'])
@login_required
def manage_tasks():
    if request.method == 'POST':
        house_id = request.form['house_id']
        company_id = request.form['company_id']

        if request.form['action'] == 'download_report':
            if house_id != '' and company_id != '':
                job = select_job(company_id, house_id)
                if job is not None:
                    company = select_description(company_id)
                    house = select_description(house_id)
                    make_word_doc(job[0], company, house)
                return jsonify({'url': url_for('data_collection.download',
                                               folder=job[0])})

        if request.form['action'] == 'show_id':
            if house_id != '' and company_id != '':
                job = select_job(company_id, house_id)
                if job is None:
                    insert_job(
                        {'company_id': company_id, 'house_id': house_id})
                    job = select_job(company_id, house_id)
                return jsonify({'id': job})
            return jsonify({'id': 'Компания или дом не выбраны'})
    return render_template('manage_tasks.html', companies=select_data(1), houses=select_data(2))


@data_collection.route("/manage_tasks/download/<folder>")
@login_required
def download(folder):
    path = f'static/data/{folder}'
    shutil.make_archive('static/data/data', 'zip', path)
    return send_file('static/data/data.zip', attachment_filename='data.zip')


@data_collection.route("/add_entity", methods=['GET', 'POST'])
@login_required
def add_entity():
    message = ''
    if request.method == 'POST':
        if request.form['source'] == 'Компания':
            insert_data({'type_id': 1, 'description': request.form['name']})
        if request.form['source'] == 'Адреc':
            insert_data({'type_id': 2, 'description': request.form['name']})
        message = 'Запись добавлена'

    return render_template('add_entity.html', message=message)
