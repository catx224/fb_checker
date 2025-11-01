# fchk.py
try:
    import importlib
    import sys, os

    # Get current directory and module name (without .py)
    module_name = os.path.splitext(os.path.basename(__file__))[0]

    # Import compiled module (.so)
    compiled_module = importlib.import_module(module_name)

    # If the compiled module has a "main" function, run it
    if hasattr(compiled_module, "fchk"):
        compiled_module.main()
    else:
        print(f"{module_name}.cpython-312.so loaded successfully.")
except Exception as e:
    print(f"Error loading compiled module: {e}")