PYTHONPATH=".:$$PYTHONPATH"
TESTSETTINGS="google_product_feeder.testsettings"

DJANGO_ADMIN="$(shell which django-admin.py)" 

COVERAGE="$(shell which coverage)"
COVERAGE_SOURCE="google_product_feeder"
COVERAGE_OMIT="migrations/*,tests/*"


test:
	PYTHONPATH=$(PYTHONPATH) DJANGO_SETTINGS_MODULE=$(TESTSETTINGS) \
		$(COVERAGE) run --source $(COVERAGE_SOURCE) --omit $(COVERAGE_OMIT) \
		$(DJANGO_ADMIN) test --settings=$(TESTSETTINGS)

coverage:
	$(COVERAGE) report -m
