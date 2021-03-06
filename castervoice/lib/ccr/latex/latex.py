'''
Created on Sep 4, 2018

@author: Mike Roberts
'''
from castervoice.lib.imports import *


# Return \first{second}, if second is empty then end inside the brackets for user input
def back_curl(first, second):
    if str(second) != "":
        return (Text("\\") + Text(str(first)) + Key("lbrace, rbrace, left") +
                Text(str(second)) + Key("right"))
    if str(second) == "":
        return (Text("\\") + Text(str(first)) + Key("lbrace, rbrace, left"))


def symbol_letters(big, symbol):
    if big:
        symbol = symbol.title()
    Text(str(symbol)).execute()


class LaTeX(MergeRule):
    pronunciation = "latex"

    mapping = {
        SymbolSpecs.COMMENT:
            R(Text("%")),
        "begin <element>":
            R(
                back_curl("begin", "%(element)s") + Key("enter:2") +
                back_curl("end", "%(element)s") + Key("up")),
        #
        "[use] package [<packages>]":
            R(back_curl("usepackage", "%(packages)s")),
        "[use] package bib latex":
            R(back_curl("usepackage[style=authoryear]", "biblatex")),
        #
        "insert [<big>] <symbol>":
            R(Text("\\") + Function(symbol_letters, extra={"big", "symbol"}) + Text(" ")),
        #
        "insert <command>":
            R(back_curl("%(command)s", "")),
        "insert <commandnoarg>":
            R(Text("\\%(commandnoarg)s")),
        "insert quotes":
            R(Text("``\'\'") + Key("left:2")),
        "insert integral":
            R(Text("\\int_{}^{}") + Key("left:4")),
        #
        "super script":
            R(Text("^") + Key("lbrace, rbrace, left")),
        "subscript":
            R(Text("_") + Key("lbrace, rbrace, left")),
        "math fraction":
            R(
                Text("\\") + Text("frac") +
                Key("lbrace, rbrace, lbrace, rbrace, space, left:4")),
        # TexStudio specific
		SymbolSpecs.COMMENT:                R(Key("c-t"), rdescript="R: Add Comment"),

        "tech":                             R(Key("as-f6"), rdescript="LaTeX: Compile LaTeX quickly"),
	    "full tech":                        R(Key("as-f7"), rdescript="LaTeX: Compile LaTeX full"),
        "are tech":                         R(Key("as-f4"), rdescript="LaTeX: Compile knitr quickly"),
	    "full are tech":                    R(Key("as-f5"), rdescript="LaTeX: Compile knitr full"),
	    "eek":                              R(Key("cs-n"), rdescript="LaTeX: Equation environment"),
		"eek align":                        R(Key("ca-l"), rdescript="LaTeX: Align environment"),
	    "numbers":                          R(Key("ca-e"), rdescript="LaTeX: Enumerate environment"),
        "items":                            R(Key("ca-i"), rdescript="LaTeX: Itemize environment"),
        "new item":                         R(Key("cs-i"), rdescript="LaTeX: New item"),
	    "emphasize it":                    	R(Key("cs-e"), rdescript="LaTeX: Emphasize text"),
        "bold it":                    	    R(Key("c-b"), rdescript="LaTeX: Bold text"),
        "leak":                             R(Key("dollar") + Key("dollar") + Key("left"), rdescript="LaTeX: In line equation"),
        "dee Frank":                    	R(Key("cs-f"), rdescript="LaTeX: Display Fraction"),
        "Frank":                    	    R(Key("as-f"), rdescript="LaTeX: Fraction"),
        "new frame":                    	R(Key("ca-f, backspace, backspace, lbrace, rbrace, enter, left"),	  rdescript="LaTeX: New beamer frame"),
	    "knitting chunk":                   R(Key("ca-k"), rdescript="LaTeX: New knitr chunk"),
	    "word count":                       R(Key("a-t, n/25, up, down, tab, enter"), rdescript="LaTeX: Word count"),
        "lay tech table":                         R(Key("cas-t"), rdescript="LaTeX: table template "),


        "new file":                         R(Key("c-n"), rdescript="TexStudio: New file"),
    	"save as":                          R(Key("ca-s"), rdescript="TexStudio: Save as"),
	 	"open recent":                      R(Key("a-f, r"), rdescript="TexStudio: Open recent"),
		"wizard quick start":               R(Key("a-w, s"), rdescript="TexStudio: Quick start"),
        # latex specific

        "lay tech infinity":                R(Text("\\infty"), rdescript="LaTeX: Infinity"),
        "lay tech shake":                   R(Text("\\\\") + Key("enter"), rdescript="LaTeX: New line"),
        "lay tech ellipses":                R(Text("\\ldots") , rdescript="LaTeX: Ellipses"),
		"Greek Alpha":                    	R(Text("\\alpha"), rdescript="LaTeX: Alpha character"),
        "Greek epsilon":                    R(Text("\\varepsilon"), rdescript="LaTeX: Alpha character"),
        "Greek Beta":                    	R(Text("\\beta"), rdescript="LaTeX: Beta character"),
        "Greek gamma":                    	R(Text("\\gamma"), rdescript="LaTeX: Small gamma character"),
        "Greek sigma":                    	R(Text("\\sigma"), rdescript="LaTeX: Small sigma character"),
        "big Greek gamma":                  R(Text("\\Gamma"), rdescript="LaTeX: Big gamma character"),
        "Greek Delta":                    	R(Text("\\delta"), rdescript="LaTeX: Small Delta character"),
        "Greek row":                    	R(Text("\\rho"), rdescript="LaTeX: Small rho character"),
        "square root":                    	R(Text("\\sqrt{")+ Key("rbrace") +Key("left"), rdescript="LaTeX: Square root"),

        "big Greek Delta":                  R(Text("\\Delta"), rdescript="LaTeX: Big Delta character"),
        "sub ex":                    	    R(Text("_{") + Key("rbrace") +Key("left"), rdescript="LaTeX: subscript"),
        "soup ex":                    	    R(Text("^{") + Key("rbrace") +Key("left"), rdescript="LaTeX: superscript"),
        "text citation":                    R(Text("\\textcite{")+  Key("rbrace")+Key("left"), rdescript="LaTeX: In text citation"),
	    "ren citation":                     R(Text("\\parencite{")+  Key("rbrace")+Key("left"), rdescript="LaTeX: Parenthesis citation"),
	    "new section":                      R(Text("\\section{") + Key("rbrace") + Key("left"), rdescript="LaTeX: New section"),
        "new sub section":                  R(Text("\\subsection{") + Key("rbrace") + Key("left"), rdescript="LaTeX: New section"),
        "lay tech degrees":                 R(Text("$^{\\circ}$"), rdescript="LaTeX: New section"),
        "lay tech curly":                   R(Text("\\left\\{\\right\\}") + Key("left") * Repeat(8), rdescript="LaTeX: Curly brackets"),
        "lay tech prekris":                 R(Text("\\left(\\right)") + Key("left") * Repeat(7), rdescript="LaTeX: Parenthesis"),
        "lay tech brax":                    R(Text("\\lef") + Key("t/25") + Key("lbracket/25") + Key("escape") + Text("\\right]") + Key("left") * Repeat(7), rdescript="LaTeX: Brackets"),
        "math bold":                        R(Text("\\bm{") + Key("rbrace") + Key("left"), rdescript="LaTeX: Bold math"),

        "quad space":                       R(Text("\\quad"), rdescript=""),
        "double quad space":                R(Text("\\qquad"), rdescript=""),
        "koom em box":                           R(Text("\\mbox{") + Key("rbrace") + Key("left"), rdescript=""),

        "koom <textnv>":                    R(Key("backslash") + Text("%(textnv)s") + Key("lbrace, rbrace, left"), rdescript="LaTeX: LaTeX command"),
        "koom sum":                    R(Key("backslash") + Text("sum_") + Key("lbrace, rbrace, left"), rdescript="LaTeX: Sum command"),
        "koom ref":                    R(Key("backslash") + Text("ref") + Key("lbrace, rbrace, left"), rdescript="LaTeX: ref command"),
        "koom (equation|eck) ref":                    R(Key("backslash") + Text("eqref") + Key("lbrace, rbrace, left"), rdescript="LaTeX: ref command"),
		"koom BM":
    		R(Key("backslash") + Text("bm") + Key("lbrace, rbrace, left"), rdescript="LaTeX: ref command"),

    }

    extras = [
        Choice("packages", {
            "math tools": "mathtools",
            "graphic ex": "graphicx",
            "wrap figure": "wrapfig",
        }),
        Choice(
            "element", {
                "center": "center",
                "columns": "columns",
                "description": "description",
                "document": "document",
                "(enumerate | numbered list)": "enumerate",
                "equation": "equation",
                "figure": "figure",
                "flush left": "flushleft",
                "flush right": "flushright",
                "frame": "frame",
                "list": "list",
                "mini page": "minipage",
                "quotation": "quotation",
                "quote": "quote",
                "table": "table",
                "title page": "titlepage",
                "verbatim": "verbatim",
                "verse": "verse",
                "wrap figure": "wrapfigure",
            }),
        Choice(
            "command", {
                "author": "author",
                "[add] bib resource": "addbibresource",
                "cancel": "cancel",
                "caption": "caption",
                "chapter": "chapter",
                "column": "column",
                "document class": "documentclass",
                "graphics path": "graphicspath",
                "[include] graphics": "includegraphics[width=1\\textwidth]",
                "label": "label",
                "new command": "newcommand",
                "paragraph": "paragraph",
                "paren cite": "parencite",
                "part": "part",
                "reference": "ref",
                "sub paragraph": "subparagraph",
                "(section | heading)": "section",
                "sub (section | heading)": "subsection",
                "sub sub (section | heading)": "subsubsection",
                "text cite": "textcite",
                "[text] bold": "textbf",
                "[text] italics": "textit",
                "[text] slanted": "textsl",
                "title": "title",
                "tilde": "tilde",
                "use theme": "usetheme",
            }),
        Choice(
            "commandnoarg", {
                "(approx | approximately) equal": "approxeq",
                "(approx | approximately)": "approx",
                "line break": "linebreak",
                "[list] item": "item",
                "make title": "maketitle",
                "new page": "newpage",
                "page break": "pagebreak",
                "print bibliography": "printbibliography",
                "table of contents": "tableofcontents",
                "text width": "textwidth",
                "partial": "partial",
                "prime": "prime",
                "no indent": "noindent",
            }),
        Choice(
            "symbol",
            {
                "alpha": "alpha",
                "beater | beta": "beta",
                "gamma": "gamma",
                "delta": "delta",
                "epsilon": "epsilon",
                "var epsilon": "varepsilon",
                "zita": "zeta",
                "eater": "eta",
                "theta": "theta",
                "iota": "iota",
                "kappa": "kappa",
                "lambda": "lambda",
                "mu": "mu",
                "new": "nu",
                "zee": "xi",
                "pie": "pi",
                "row": "rho",
                "sigma": "sigma",
                "tau": "tau",
                "upsilon": "upsilon",
                "phi": "phi",
                "chi": "chi",
                "sigh": "psi",
                "omega": "omega",
                #
                "times": "times",
                "divide": "div",
                "intersection": "cap",
                "union": "cup",
                "stop": "cdot",
                "approximate": "approx",
                "proportional": "propto",
                "not equal": "neq",
                "member": "in",
                "for all": "forall",
                "partial": "partial",
                "infinity": "infty",
                "dots": "dots",
                #
                "left arrow": "leftarrow",
                "right arrow": "rightarrow",
                "up arrow": "uparrow",
                "down arrow": "downarrow",
                #
                "left": "left(",
                "right": "right)",
            }),
        Choice("big", {
            "big": True,
        }),
        Dictation("textnv"),
        IntegerRefST("n", 1, 10000),
    ]
    defaults = {
        "big": False,
        "packages": "",
    }


control.global_rule(LaTeX())
