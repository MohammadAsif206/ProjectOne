import  logging
from flask import Flask
from routes.employee_route import create_employee_route
from routes.erequest_route import create_erequest_route

app: Flask = Flask(__name__)
create_employee_route(app)
create_erequest_route(app)

logging.basicConfig(filename="record.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

if __name__ == '__main__':
    app.run(debug=True)























































































