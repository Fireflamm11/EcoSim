.PHONY: install
install:
	git config core.hooksPath .git/hooks
	rm -fr .git/hooks/* || true
	cp -a .githooks/* .git/hooks

.PHONY: lint
lint:
	flake8 --config=.flake8

.PHONY: test
test:
	pytest -v $(TEST_DIR)/