python = python
library ?= ${BIB}
text =  intro-to-mvpa.md
#mdflags ?= -f markdown-hard_line_breaks+yaml_metadata_block
refs ?= refs.bib

%.md: %.Rmd
	R --vanilla --slave -e 'knitr::knit("$<")'
	
%-handout.pdf: %.md
	pandoc -o $* $<

cluster.pdf scatter.pdf color_scatter.pdf: intro-to-mvpa.py
	python intro-to-mvpa.py

intro-to-mvpa-slides.pdf: intro-to-mvpa.md $(refs) cluster.pdf scatter.pdf
	pandoc -o $@ $< --to="beamer" --slide-level=2 --include-in-header="surface.tex" --latex-engine=xelatex --bibliography=$(refs)
 
# intro-to-eep-erp-slides.pdf
%-slides.pdf: %.md
	pandoc -o $@ $< --to="beamer" --slide-level=2 --include-in-header="surface.tex" --latex-engine=xelatex

$(refs): bib.keys $(library)
ifeq ($(library),)
	@echo "No library specified, skipping generation of new bibliography"
else
	$(python) extractbib.py bib.keys $(library) $(refs)
endif

bib.keys: $(text) $(library)
	egrep '@[-:_a-zA-Z0-9.]*' $(text) -oh --color=never | sort -u | sed 's/@//g' > bib.keys