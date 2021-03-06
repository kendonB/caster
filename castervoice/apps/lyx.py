from castervoice.lib.imports import *


class LyxRule(MergeRule):
    pronunciation = "lyx"

    mapping = {
        "new file": R(Key("c-n")),
        "open file": R(Key("c-o")),
        "save as": R(Key("cs-s")),
        "math mode": R(Key("c-m")),
        "display mode": R(Key("cs-m")),
        "view PDF": R(Key("c-r")),
        "update PDF": R(Key("cs-r")),
        "move line up [<n>]": R(Key("a-up"))*Repeat(extra="n"),
        "move line down [<n>]": R(Key("a-down"))*Repeat(extra="n"),
        "insert <environment>": R(Key("a-i, h, %(environment)s")),
    }
    extras = [
        IntegerRefST("n", 1, 10),
        Choice(
            "environment", {
                "(in line formula | in line)": "i",
                "(display formula | display)": "d",
                "(equation array environment | equation array)": "e",
                "(AMS align environment | AMS align)": "a",
                "AMS align at [environment]": "t",
                "AMS flalign [environment]": "f",
                "(AMS gathered environment | AMS gather)": "g",
                "(AMS multi line [environment]| multiline)": "m",
                "array [environment]": "y",
                "(cases [environment] | piece wise)": "c",
                "(aligned [environment] | align)": "l",
                "aligned at [environment]": "v",
                "gathered [environment]": "h",
                "split [environment]": "s",
                "delimiters": "r",
                "matrix": "x",
                "macro": "o",
            }),
    ]
    defaults = {
        "n": 1,
    }


context = AppContext(executable="lyx")
control.non_ccr_app_rule(LyxRule(), context=context)
