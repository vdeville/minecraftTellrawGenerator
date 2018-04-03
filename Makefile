clean:
	rm -rf build/ dist/

release:
	python setup.py sdist bdist_wheel
	twine upload dist/*

release_test: clean
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
