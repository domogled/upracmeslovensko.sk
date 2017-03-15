#!/usr/bin/env python3

import livereload

import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler, PatternMatchingEventHandler

# import index

class UklidmeCesko_Handler(PatternMatchingEventHandler):
    
    def __init__(self):
        super().__init__(patterns=['*.py', '*.php'], ignore_patterns=['__pycache__', '*.pyc'], ignore_directories=True, case_sensitive=True)

    # def dispatch(self, event):
    #     print('dispatch', event)
    #     super().dispatch(event)

    def on_any_event(self, event):
        print('any event', event)

my_event_handler = UklidmeCesko_Handler()

from index import main as parse_index

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else './src'
    event_handler = LoggingEventHandler()
    observer = Observer()
    w = observer.schedule(my_event_handler, path, recursive=True)
    # print('observerd pwatch', w)
    observer.add_handler_for_watch(event_handler, w)
    observer.start()

    parse_index()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()