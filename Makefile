clean:
	rm -rf build/ dist/ *egg-info/

release: build
	twine upload dist/*

release_test: build
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

build: clean
	python setup.py sdist bdist_wheel

