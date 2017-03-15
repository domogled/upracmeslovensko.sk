#!/usr/bin/env sh

# watchexec -c -w ./pruga -e py,php "$1"

# watchmedo  shell-command --command='echo "${watch_src_path}"' --recursive src

watchmedo  shell-command --command='./dev.py' --recursive src

# watchexec -c -w ./php -e py,php "php php/dev_utils/make_ast_py.php"

# watchexec -c -w ./pruga -e py,php "pruga/scripts/eval_php_ast_json.py ./php/wordpress/www.ast/index.php"


