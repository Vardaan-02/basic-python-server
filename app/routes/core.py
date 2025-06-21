from flask import Blueprint
from app.controllers.core_controller import (
    get_home, get_health, get_time, get_location, post_greet
)

core_bp = Blueprint('core', __name__)

core_bp.route('/', methods=['GET'])(get_home)
core_bp.route('/health', methods=['GET'])(get_health)
core_bp.route('/time', methods=['GET'])(get_time)
core_bp.route('/location', methods=['GET'])(get_location)
core_bp.route('/greet', methods=['POST'])(post_greet)
