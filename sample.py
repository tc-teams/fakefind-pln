from app import create_app
from flask_script import Manager

sample = Manager(create_app)


if __name__ == '__main__':
   sample.run()