import json

from flask import Blueprint, Flask, render_template

from src.api.controllers.dataset_controller import get_2020_dataset_columns
# Set the template folder explicitly when initializing the Flask app
app = Flask(__name__, template_folder='/home/ivy/feature_importance_service/flask_app/frontend')

base_blueprint = Blueprint('base', __name__)


@base_blueprint.route('/', methods=['GET'])
def get_dashboard():
    columns = get_2020_dataset_columns()
    return render_template('index.html', columns=json.dumps(columns))
