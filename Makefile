%.md: %.Rmd
	R --vanilla --slave -e 'knitr::knit("$<")'
	
%-handout.pdf: %.md
	pandoc -o $* $<

cluster.pdf scatter.pdf: intro-to-mvpa.py
	python intro-to-mvpa.py

intro-to-mvpa-slides.pdf: intro-to-mvpa.md cluster.pdf scatter.pdf
	pandoc -o $@ $< --to="beamer" --slide-level=2 --include-in-header="surface.tex" --latex-engine=xelatex
 
# intro-to-eep-erp-slides.pdf
%-slides.pdf: %.md
	pandoc -o $@ $< --to="beamer" --slide-level=2 --include-in-header="surface.tex" --latex-engine=xelatex
	