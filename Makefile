clean:
	rm -rf .coverage cover nosetests.xml coverage.xml .tox *.egg-info
	find . -name '*.pyc' -exec rm '{}' ';'
	find . -name '__pycache__' -exec rm -rf {} \;