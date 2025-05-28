import ast

class PythonToCppCompiler(ast.NodeVisitor):
    def __init__(self):
        self.cpp_lines = []
        self.indent = 0
        self.variables = {}

    def write_line(self, line):
        self.cpp_lines.append('    ' * self.indent + line)

    def compile(self, code):
        tree = ast.parse(code)
        self.cpp_lines.append('#include <iostream>')
        self.cpp_lines.append('using namespace std;')
        self.cpp_lines.append('')
        self.cpp_lines.append('int main() {')
        self.indent += 1
        self.visit(tree)
        self.write_line('return 0;')
        self.indent -= 1
        self.cpp_lines.append('}')
        return '\n'.join(self.cpp_lines)






