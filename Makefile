%.md: %.Rmd
	R --vanilla --slave -e 'knitr::knit("$<")'
	
%-handout.pdf: %.md
	pandoc -o $* $<

%-slides.pdf: %.md
	pandoc -o $@ $< --to="beamer" --slide-level=2 --include-in-header="surface.tex" --latex-engine=xelatex
	