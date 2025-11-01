#!/usr/bin/env python3
"""
Dev Mueid Mursalin Rifat
"""

import sys
import os
from pathlib import Path

def main():
    # Add current directory to Python path
    current_dir = Path(__file__).parent
    sys.path.insert(0, str(current_dir))
    
    try:
        # Import the compiled module
        import fchk
        
        # If the module has a main function, call it
        if hasattr(fchk, 'main'):
            fchk.main()
        elif hasattr(fchk, 'run'):
            fchk.run()
        else:
            # Try to call it as a function if it's callable
            if callable(fchk):
                fchk()
            else:
                print("fchk module loaded successfully!")
                print("Available functions:", [x for x in dir(fchk) if not x.startswith('_')])
                
    except ImportError as e:
        print(f"Error importing fchk module: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error running fchk: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
