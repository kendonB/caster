from dragonfly import Choice, Repeat

from castervoice.lib import control
from castervoice.lib.actions import Key, Text
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge.ccrmerger import CCRMerger
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R


class Punctuation(MergeRule):
    pronunciation = CCRMerger.CORE[3]

    mapping = {
        "[<long>] <single_character>": R(Text("%(long)s" + "%(single_character)s" + "%(long)s")),
        "quotes":
            R(Key("dquote,dquote,left"), rdescript="Core: Quotation Marks"),
        "thin quotes":
            R(Key("apostrophe,apostrophe,left"), rdescript="Core: Thin Quotation Marks"),
        "bakes":
            R(Key("backtick, backtick, left"), rdescript="Core: Backtick Pair"),
        "prekris":
            R(Key("lparen, rparen, left"), rdescript="Core: Parentheses"),
        "brax":
            R(Key("lbracket, rbracket, left"), rdescript="Core: Square Brackets"),
        "curly":
            R(Key("lbrace, rbrace, left"), rdescript="Core: Curly Braces"),
        "angle":
            R(Key("langle, rangle, left"), rdescript="Core: Angle Brackets"),
        'tabby [<npunc>]':
            R(Key("tab"), rdescript="Core: Tab")*Repeat(extra="npunc"),
        'lay tabby [<npunc>]':
            R(Key("s-tab"), rdescript="Core: Shift Tab")*Repeat(extra="npunc"),
        "boom":
            R(Text(", "), rdescript="Core: Comma + Space"),
		"ren":
            R(Key("lparen"), rdescript="Core: Left Parentheses"),
		"glow ren":
            R(Key("rparen"), rdescript="Core: Right Parentheses"),
		"bray":
            R(Key("lbrace"), rdescript="Core: Left Brace"),
		"glow bray":
            R(Key("rbrace"), rdescript="Core: Right Brace"),
		

    }

    extras = [
        IntegerRefST("npunc", 0, 10),
        Choice("long", {
               "long": " ",
        }),
        Choice("single_character", {
               "semper":                               ";",
               "[is] greater than":                    ">",  
               "[is] less than":                       "<",
               "[is] greater [than] [or] equal [to]": ">=",
               "[is] less [than] [or] equal [to]":    "<=",
               "[is] equal to":                       "==",
               "equals":                               "=",
               "plus":                                 "+",
               "minus":                                "-",
               "pipe (sim | symbol)":                  "|",
               "ace":                                  " ",
               "clamor":                               "!",     
               "deckle":                               ":",
               "starling":                             "*",  
               "questo":                               "?", 
               "comma":                                ",",  
               "carrot":                               "^", 
               "(period | dot)":                       ".", 
               "at E":                                 "@", 
               "hash tag":                             "#",
               "apostrophe | single quote":            "'",   
               "underscore":                           "_",
               "backslash":                           "\\", 
               "slash":                                "/",
               "Dolly":                                "$",
               "modulo":                               "%",
               "ampersand":                            "&",
               "tilde":                                "~",
               "(left prekris | lay)":                 "(",
               "(right prekris | ray)":                ")",
               "(left brax | lack)":                   "[",
               "(right brax | rack)":                  "]",
               "(left angle | lang)":                  "<",
               "(right angle | rang)":                 ">",
               "(left curly | lace)":                  "{",
               "(right curly | race)":                 "}",

        }),
    ]
    defaults = {
        "npunc": 1,
        "long": "",
    }


        
control.nexus().merger.add_global_rule(Punctuation())
