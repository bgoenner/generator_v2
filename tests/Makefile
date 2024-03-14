# Shell setup for make
SHELL      	= /bin/bash

.SHELLFLAGS	= -o pipefail -c

# Default target when invoking without specific target.
.DEFAULT_GOAL := all

include ./config.mk

DEF_FILE = ./../def_test/test_1_2in.def
TLEF     = ./../def_test/test_1.tlef

render: 
	mkdir -p ./../test_output/make_test
	python3 ./../generator_v2.py $(SCAD_ARGS) \
		--def_file  $(DEF_FILE) \
		--design "$(DESIGN)" \
		--tlef $(TLEF) \
		--results_dir ./../test_output/make_test

all: render