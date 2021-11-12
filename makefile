ACTIVATE := ./HFenv/bin/activate
PYTHON := python3
ifeq '$(findstring ;,$(PATH))' ';'
	ACTIVATE := .\HFenv\Scripts\activate
	PYTHON := python
endif

.PHONY: venv
venv:
	$(PYTHON) -m venv HFenv


run:
	$(ACTIVATE)
	$(PYTHON) app.py