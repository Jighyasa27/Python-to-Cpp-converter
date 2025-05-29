def visit_BinOp(self, node):
    return f'({self.visit(node.left)} {self.visit(node.op)} {self.visit(node.right)})'

def visit_Compare(self, node):
    return f'{self.visit(node.left)} {self.visit(node.ops[0])} {self.visit(node.comparators[0])}'

def visit_Call(self, node):
    return f'{node.func.id}({", ".join([self.visit(arg) for arg in node.args])})'

def visit_Name(self, node):
    return node.id

def visit_Constant(self, node):
    return f'"{node.value}"' if isinstance(node.value, str) else str(node.value)

# Operators

def visit_Add(self, node): return '+'
def visit_Sub(self, node): return '-'
def visit_Mult(self, node): return '*'
def visit_Div(self, node): return '/'
def visit_Lt(self, node): return '<'
def visit_Gt(self, node): return '>'
def visit_Eq(self, node): return '=='



def visit_BoolOp(self, node):
    op = self.visit(node.op)
    values = [self.visit(v) for v in node.values]
    return f' {op} '.join(values)

def visit_And(self, node):
    return '&&'

def visit_Or(self, node):
    return '||'


# --- New: Unary Operations ---

def visit_UnaryOp(self, node):
    return f'({self.visit(node.op)}{self.visit(node.operand)})'

def visit_Not(self, node):
    return '!'

def visit_USub(self, node):  # Unary minus
    return '-'

def visit_UAdd(self, node):  # Unary plus
    return '+'

