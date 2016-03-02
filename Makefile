python = python
library ?= ${BIB}
text =  intro-to-mvpa.md
#mdflags ?= -f markdown-hard_line_breaks+yaml_metadata_block
refs ?= refs.bib
pyfigs = cluster.pdf color_scatter_pca.pdf color_scatter.pdf color_scatter_test.pdf kmeans.pdf scatter_big_train.pdf scatter_big_train_svm.pdf scatter_big_test.pdf scatter_big_test_svm.pdf scatter.pdf svm_test.pdf svm_train.pdf
	
%-handout.pdf: %.md
	pandoc -o $* $<

$(pyfigs): intro-to-mvpa.py
	python intro-to-mvpa.py

intro-to-mvpa-slides.pdf: intro-to-mvpa.md $(refs) $(pyfigs)
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