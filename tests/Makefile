TESTS = $(wildcard test_*.py)

#  XXX Uncomment these lines if you want to test with Python 3.2 and 3.3
#all.PHONY: test test32 test33
#
#test32:
#	@- $(foreach TEST,$(TESTS), \
#		echo === Running python3 test: $(TEST); \
#		python3.2 $(TEST); \
#		)
#test33:
#	@- $(foreach TEST,$(TESTS), \
#		echo === Running python3 test: $(TEST); \
#		python3.3 $(TEST); \
#		)

.PHONY: test

test:
	@- $(foreach TEST,$(TESTS), \
		echo === Running test: $(TEST); \
		python $(TEST); \
		)
