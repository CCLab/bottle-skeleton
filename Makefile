.PHONY: default

default: lint


LIB = ./app/*py
APP = ./main.py
CSS = ./static/css/*css
JS  = ./static/js/*js

lint: $(APP) $(LIB) $(JS)
	@echo "-------------------------------"
	@echo ">>> Checking python source code"
	@echo "-------------------------------"
	pychecker --limit 30 $(APP) $(LIB)

	@echo ""
	@echo "---------------------------"
	@echo ">>> Checking js source code"
	@echo "---------------------------"
	jslint --white --sub --nomen --vars --predef $$ $(JS)

	@echo ""
	@echo "---------------------------------------------"
	@echo ">>> The code is clean - you can commit it now"
	@echo "---------------------------------------------"

run: $(APP)
	python $(APP) dev
