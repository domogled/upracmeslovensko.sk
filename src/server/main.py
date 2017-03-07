#!/usr/bin/env python3

"""
Demo for the live reloading of Sanic server.
"""
# from __future__ import absolute_import

# Standard imports
import os
import sys

from sanic import Sanic
from sanic.response import text

import livereload

def main():
    """
    Main function.

    :return:
        None.
    """
    try:

        # Server host
        # server_host = '0.0.0.0'
        server_host = 'upracmeslovensko.dev'

        # Server port
        server_port = 8081

        DEBUG = True

        # Get message
        msg = f'# ----- Run server -----\nHost: {server_host}\nPort: {server_port}\nDebug: {DEBUG}'

        # Print message
        print(msg)
        
        # Create Sanic app
        sanic_app = Sanic()

        # Create request handler
        @sanic_app.route('/api/')
        async def hello_handler(request):  # pylint: disable=unused-variable
            """
            Request handler.

            :return:
                Response body.
            """
            # Return response body
            return text('Upracme Slovensko')

        @sanic_app.route('/onas/<p>')
        async def hello_handler(request, p):  # pylint: disable=unused-variable
            """
            Request handler.

            :return:
                Response body.
            """
            # Return response body
            return text(f'O nás {p}')

        # Run server.
        #
        # Notice `KeyboardInterrupt` will be caught inside `sanic_app.run`.
        #
        sanic_app.run(
            host=server_host,
            port=server_port,
            debug = DEBUG
        )

    # If have `KeyboardInterrupt`
    except KeyboardInterrupt:
        # Not treat as error
        pass


# If is run as main module
if __name__ == '__main__':
    # Call main function
    exit(main())