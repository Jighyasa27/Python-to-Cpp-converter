from util.core import PythonToCppCompiler 
import util.statements as stmts
import util.expressions as exprs
import util.functions as funcs

# Bind visitor methods from all modules to the compiler class
for name in dir(stmts):
    if name.startswith("visit_"):
        setattr(PythonToCppCompiler, name, getattr(stmts, name))

for name in dir(exprs):
    if name.startswith("visit_"):
        setattr(PythonToCppCompiler, name, getattr(exprs, name))

for name in dir(funcs):
    if name.startswith("visit_"):
        setattr(PythonToCppCompiler, name, getattr(funcs, name))


if __name__ == '__main__':
    mode = input("Choose input method (file/manual): ").strip().lower()

    if mode == 'file':
        filename = input("Enter Python source filename: ").strip()
        filename = r"test\\" + filename + ".py"
        print(f"Reading from file: {filename}")
        try:
            with open(filename, 'r') as f:
                py_code = f.read()
        except FileNotFoundError:
            print("❌ File not found.")
            exit(1)
    elif mode == 'manual':
        print("Enter your Python code (end with a blank line):")
        lines = []
        while True:
            try:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)
            except EOFError:
                break  # Handle Ctrl+D to end input
        py_code = "\n".join(lines)
    else:
        print("❌ Invalid input method. Please choose 'file' or 'manual'.")
        exit(1)

    # Compile Python to C++
    compiler = PythonToCppCompiler()
    cpp_code = compiler.compile(py_code)

    # Print the result
    print("\n--- ✅ Generated C++ Code ---\n")
    print(cpp_code)

    # Ask where to save
    output_filename = input("\nEnter output filename (default: result.cpp): ").strip()
    if not output_filename:
        output_filename = "result"

    output_filename = r"output\\" + output_filename + ".cpp"

    try:
        with open(output_filename, 'w') as f:
            f.write(cpp_code)
        print(f"\n✅ C++ code saved to: {output_filename}")
    except Exception as e:
        print(f"❌ Error saving file: {e}")