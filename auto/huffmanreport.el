(TeX-add-style-hook
 "huffmanreport"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "paper=a4" "fontsize=10pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("babel" "english") ("algpseudocode" "noend") ("geometry" "margin=1in")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "inputenc"
    "babel"
    "amsmath"
    "amsfonts"
    "amsthm"
    "graphicx"
    "tikz"
    "algorithm"
    "algpseudocode"
    "geometry")
   (TeX-add-symbols
    "BState")
   (LaTeX-add-labels
    "alg:huffman"
    "fig:subopt"
    "alg:dec")
   (LaTeX-add-bibitems
    "huffman52"
    "mackay"))
 :latex)

