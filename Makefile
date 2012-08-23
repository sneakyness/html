dummy:

all: html 2dcontext
html: output/html/Overview.html
2dcontext: output/2dcontext/Overview.html

output/html/Overview.html: source
	python scripts/publish.py html

output/2dcontext/Overview.html: source
	python scripts/publish.py 2dcontext
