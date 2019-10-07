deps:
	@pip install -r requirements.txt

start:
	@python main.py

populate:
	@python populate.py

releasedb:
	@rm -rf sqlite.db