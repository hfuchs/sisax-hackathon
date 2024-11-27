#
# 2024-11-27, Created by H Fuchs <code@hfuchs.net>
#
# Purpose: Run venv'd Python project
#

entrypoint := skat.py

run: venv
	. venv/bin/activate; python $(entrypoint)

debug: test
test: venv
	. venv/bin/activate; python $(entrypoint) --debug

ipython: venv
	. venv/bin/activate; ipython3

venv: venv/touchfile

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

clean:
	rm -rf venv
	find -iname "*.pyc" -delete
	rm -rf *pdf *png *jpg
