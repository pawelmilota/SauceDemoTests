.PHONY = run_specific run_all install

.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "To install all requirements : make install"
	@echo "To run specific test: make run_specific TEST_NAME=<test_name>"
	@echo "To run all tests: make run_all"
	@echo "------------------------------------"

run_specific $(TEST_NAME):
	pytest -vv -k $(TEST_NAME)

run_all:
	pytest -vv -m UI

install:
	pip install -r .\requirements.txt
