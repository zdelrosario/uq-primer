filename=primer
name1=ch1-introduction
name2=ch2-demonstration
name3=ch3-exploration

main:
	pdflatex -aux-directory=aux --shell-escape -output-directory=aux ${filename}
	bibtex aux/${filename}
	pdflatex -aux-directory=aux -output-directory=aux ${filename}
	pdflatex -aux-directory=aux -output-directory=aux ${filename}

	mv aux/${filename}.pdf .

clean:
	rm -f aux/${filename}.{log,aux,out,bbl,blg,fls,ilg,nlo,idx,lof,lot,nav,snm,toc,nls}
	rm -f aux/${name1}.{log,aux,out,bbl,blg,fls,ilg,nlo,idx,lof,lot,nav,snm,toc,nls}
	rm -f aux/${filename}.fdb_latexmk
	rm -f aux/.${filename}.tex.swp

ch1:
	pdflatex -aux-directory=aux -output-directory=aux tex/${name1}
	mv aux/${name1}.pdf .

ch2:
	pdflatex -aux-directory=aux -output-directory=aux tex/${name2}
	mv aux/${name2}.pdf .

ch3:
	pdflatex -aux-directory=aux -output-directory=aux tex/${name3}
	mv aux/${name3}.pdf .

links:
	cp -f ~/Git/zachs_macros/zachs_macros.tex ./tex/zachs_macros.tex
	cp -f ~/Git/zachs_macros/numdef.sty numdef.sty
	cp -f ~/Git/pi_space/pubs.bib ./tex/pubs.bib
