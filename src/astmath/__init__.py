"""astmath - Evaluate arithemetic expressions safely."""
import ast
import builtins


def eval(source: str) -> object:
    """Evaluates constant expressions without executing any code."""

    try:
        tree = ast.parse(source, mode="eval")
    except SyntaxError:
        raise ValueError("astmath.eval(...) only supports single expressions.")

    return ArithemeticCalculator().visit(tree)


class ArithemeticCalculator(ast.NodeTransformer):
    def visit_Expression(self, node: ast.Expression) -> object:
        super().generic_visit(node)
        if isinstance(node.body, ast.Constant):
            return node.body.value

        raise ValueError("astmath.eval(...) doesn't work on non-constants.")

    def visit_BinOp(self, node: ast.BinOp) -> ast.Constant:
        super().generic_visit(node)
        if isinstance(node.left, ast.Constant) and isinstance(node.right, ast.Constant):
            return ast.Constant(builtins.eval(ast.unparse(node)))

        raise ValueError("astmath.eval(...) doesn't work on non-constants.")
