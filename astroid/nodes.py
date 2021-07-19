# Copyright (c) 2006-2011, 2013 LOGILAB S.A. (Paris, FRANCE) <contact@logilab.fr>
# Copyright (c) 2010 Daniel Harding <dharding@gmail.com>
# Copyright (c) 2014-2020 Claudiu Popa <pcmanticore@gmail.com>
# Copyright (c) 2014 Google, Inc.
# Copyright (c) 2015-2016 Ceridwen <ceridwenv@gmail.com>
# Copyright (c) 2016 Jared Garst <jgarst@users.noreply.github.com>
# Copyright (c) 2017 Ashley Whetter <ashley@awhetter.co.uk>
# Copyright (c) 2017 rr- <rr-@sakuya.pl>
# Copyright (c) 2018 Bryce Guinta <bryce.paul.guinta@gmail.com>
# Copyright (c) 2021 Pierre Sassoulas <pierre.sassoulas@gmail.com>
# Copyright (c) 2021 Marc Mueller <30130371+cdce8p@users.noreply.github.com>

# Licensed under the LGPL: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
# For details: https://github.com/PyCQA/astroid/blob/main/LICENSE

"""Every available node class.

.. seealso::
    :doc:`ast documentation <green_tree_snakes:nodes>`

All nodes inherit from :class:`~astroid.node_classes.NodeNG`.
"""

# Nodes not present in the builtin ast module:  DictUnpack, Unknown, and EvaluatedObject.

from astroid.node_classes import (  # pylint: disable=redefined-builtin (Ellipsis)
    AnnAssign,
    Arguments,
    Assert,
    Assign,
    AssignAttr,
    AssignName,
    AsyncFor,
    AsyncWith,
    Attribute,
    AugAssign,
    Await,
    BinOp,
    BoolOp,
    Break,
    Call,
    Compare,
    Comprehension,
    Const,
    Continue,
    Decorators,
    DelAttr,
    Delete,
    DelName,
    Dict,
    DictUnpack,
    Ellipsis,
    EmptyNode,
    EvaluatedObject,
    ExceptHandler,
    Expr,
    ExtSlice,
    For,
    FormattedValue,
    Global,
    If,
    IfExp,
    Import,
    ImportFrom,
    Index,
    JoinedStr,
    Keyword,
    List,
    Match,
    MatchAs,
    MatchCase,
    MatchClass,
    MatchMapping,
    MatchOr,
    MatchSequence,
    MatchSingleton,
    MatchStar,
    MatchValue,
    Name,
    NamedExpr,
    NodeNG,
    Nonlocal,
    Pass,
    Raise,
    Return,
    Set,
    Slice,
    Starred,
    Subscript,
    TryExcept,
    TryFinally,
    Tuple,
    UnaryOp,
    Unknown,
    While,
    With,
    Yield,
    YieldFrom,
    const_factory,
)
from astroid.scoped_nodes import (
    AsyncFunctionDef,
    ClassDef,
    DictComp,
    FunctionDef,
    GeneratorExp,
    Lambda,
    ListComp,
    Module,
    SetComp,
)

ALL_NODE_CLASSES = (
    AnnAssign,
    Arguments,
    Assert,
    Assign,
    AssignAttr,
    AssignName,
    AsyncFor,
    AsyncFunctionDef,
    AsyncWith,
    Attribute,
    AugAssign,
    Await,
    BinOp,
    BoolOp,
    Break,
    Call,
    ClassDef,
    Compare,
    Comprehension,
    Const,
    const_factory,
    Continue,
    Decorators,
    DelAttr,
    Delete,
    DelName,
    Dict,
    DictComp,
    DictUnpack,
    Ellipsis,
    EmptyNode,
    EvaluatedObject,
    ExceptHandler,
    Expr,
    ExtSlice,
    For,
    FormattedValue,
    FunctionDef,
    GeneratorExp,
    Global,
    If,
    IfExp,
    Import,
    ImportFrom,
    Index,
    JoinedStr,
    Keyword,
    Lambda,
    List,
    ListComp,
    Match,
    MatchAs,
    MatchCase,
    MatchClass,
    MatchMapping,
    MatchOr,
    MatchSequence,
    MatchSingleton,
    MatchStar,
    MatchValue,
    Module,
    Name,
    NamedExpr,
    NodeNG,
    Nonlocal,
    Pass,
    Raise,
    Return,
    Set,
    SetComp,
    Slice,
    Starred,
    Subscript,
    TryExcept,
    TryFinally,
    Tuple,
    UnaryOp,
    Unknown,
    While,
    With,
    Yield,
    YieldFrom,
)

__all__ = (
    "AnnAssign",
    "Arguments",
    "Assert",
    "Assign",
    "AssignAttr",
    "AssignName",
    "AsyncFor",
    "AsyncFunctionDef",
    "AsyncWith",
    "Attribute",
    "AugAssign",
    "Await",
    "BinOp",
    "BoolOp",
    "Break",
    "Call",
    "ClassDef",
    "Compare",
    "Comprehension",
    "Const",
    "const_factory",
    "Continue",
    "Decorators",
    "DelAttr",
    "Delete",
    "DelName",
    "Dict",
    "DictComp",
    "DictUnpack",
    "Ellipsis",
    "EmptyNode",
    "EvaluatedObject",
    "ExceptHandler",
    "Expr",
    "ExtSlice",
    "For",
    "FormattedValue",
    "FunctionDef",
    "GeneratorExp",
    "Global",
    "If",
    "IfExp",
    "Import",
    "ImportFrom",
    "Index",
    "JoinedStr",
    "Keyword",
    "Lambda",
    "List",
    "ListComp",
    "Match",
    "MatchAs",
    "MatchCase",
    "MatchClass",
    "MatchMapping",
    "MatchOr",
    "MatchSequence",
    "MatchSingleton",
    "MatchStar",
    "MatchValue",
    "Module",
    "Name",
    "NamedExpr",
    "NodeNG",
    "Nonlocal",
    "Pass",
    "Raise",
    "Return",
    "Set",
    "SetComp",
    "Slice",
    "Starred",
    "Subscript",
    "TryExcept",
    "TryFinally",
    "Tuple",
    "UnaryOp",
    "Unknown",
    "While",
    "With",
    "Yield",
    "YieldFrom",
)
