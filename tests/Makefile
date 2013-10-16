TESTS = $(wildcard test_*.py)

.PHONY: test

test:
	@- $(foreach TEST,$(TESTS), \
		echo === Running test: $(TEST); \
		python $(TEST); \
		)
