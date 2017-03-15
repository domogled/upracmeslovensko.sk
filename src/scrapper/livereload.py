
import sys

from pathlib import Path

try:
    # to src_path2/src directory
    src_path = Path(__file__).parents[1].resolve()
   
    print(f'# ----- Live reload -----')
    print(f"livereload watch {src_path}")
    
    # If the `src` directory path is not in `sys.path`
    if src_path not in sys.path:
        # Add to `sys.path`.
        #
        # This aims to save user setting PYTHONPATH when running this demo.
        #
        sys.path.append(src_path)

    # Import reloader class
    from aoiklivereload import LiveReloader

    # Create reloader
    reloader = LiveReloader()

    # Start watcher thread
    reloader.start_watcher_thread()

except KeyboardInterrupt:
        # Not treat as error
        pass