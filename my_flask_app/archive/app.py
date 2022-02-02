
from scripts.__init__ import create_app
from scripts.settings import MONGO_URI

if __name__ == "__main__":
	app = create_app()
	app.config['MONGO_URI'] = MONGO_URI
	app.run(debug=True)


