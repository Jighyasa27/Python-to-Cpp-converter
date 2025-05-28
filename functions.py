def visit_FunctionDef(self, node):
    args = ', '.join(['auto ' + arg.arg for arg in node.args.args])
    self.write_line(f'auto {node.name}({args}) {{')
    self.indent += 1
    for stmt in node.body:
        self.visit(stmt)
    self.write_line('return 0;')
    self.indent -= 1
    self.write_line('}')