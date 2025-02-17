from flask import Blueprint, jsonify, request

from src.api.controllers import dataset_controller

dataset_blueprint = Blueprint('dataset', __name__, url_prefix='/dataset')


@dataset_blueprint.route('/<dataset>/boxplots', methods=['GET'])
def get_all_boxplots(dataset):
    return dataset_controller.get_all_boxplots(dataset)

@dataset_blueprint.route('/<dataset>/piecharts', methods=['GET'])
def get_piecharts(dataset):
    return dataset_controller.get_all_piecharts(dataset)

@dataset_blueprint.route('/<dataset>/barcharts', methods=['GET'])
def get_barcharts(dataset):
    return dataset_controller.get_all_barcharts(dataset)

