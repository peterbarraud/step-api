import json
from flask import Flask # be careful that's Flask with F caps
import documentmodel as dom
from logger import APILogger

APP = Flask(__name__)


@APP.route("/test")
def get_started():
    logger = APILogger();
    ret_val = []
    step_file = r"C:\Users\barraud\Downloads\grade-my-assignment\samples\StudentExample2ApplicationProtocol_214.stp"
    document = dom.get_document_object(step_file)
    for key, value in document.getEntitiesByNameDict().items():
        ret_val.append(value[0].name)
    cp = document.getEntityById(569)
    return json.dumps(ret_val)


if __name__ == "__main__":
    APP.run()