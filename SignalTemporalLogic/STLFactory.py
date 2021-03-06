
#Class to construct and recognize STL rules using parser and lexer
from antlr4 import * #CommonTokenStream
from SignalTemporalLogic.SignalTemporalLogicParser import SignalTemporalLogicParser
from SignalTemporalLogic.SignalTemporalLogicLexer import SignalTemporalLogicLexer
from SignalTemporalLogic.STLExtendedVisitor import STLExtendedVisitor
from STLTree.STLTree import STLTree
import treelib as treelib
import logging

class STLFactory:
    def __init__(self):
        pass

    def constructFormulaTree(self, rule):
        lex = SignalTemporalLogicLexer(InputStream(rule))
        tokens = CommonTokenStream(lex)
        parser = SignalTemporalLogicParser(tokens)
        tree = parser.evl()

        try:
            result, formulaTree = STLExtendedVisitor().visit(tree)
            # formulaTree.show()
            # formulaTree.printTree()
            return formulaTree
        except:
            logging.error("ERROR parsing tree, improper formula supplied")
            logging.error("Rule supplied was: " + '%s' % str(rule))
            return None



def main():
    factory = STLFactory()

    #rule = "F[0, 300] (G[0,100] x <= 33 | y >= 20)\n"
    #rule = "F[0,100] (x <= 33 -> y >= 20) -> G[10,10](x>10)"
    rule = "(F[0, 300] (G[0,100] (-30.0 <= x | y >= -20)))\n ((z > -4) U[0,20] (q > 3))\n"
    #rule = "G[10,20] (x> 4 | y < 12)  & F[10, 10] (v < 10)\n"


    factory.constructFormulaTree(rule)


if __name__ == '__main__':
    main()
