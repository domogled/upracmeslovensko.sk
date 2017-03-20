#!/usr/bin/env sh

# watchexec -c -w ./pruga -e py,php "$1"

# watchmedo  shell-command --command='echo "${watch_src_path}"' --recursive src

# watchmedo  shell-command --command='./src/scrapper/index.py' --recursive src

# watchexec -c -w ./php -e py,php "php php/dev_utils/make_ast_py.php"

# watchexec -c -w ./pruga -e py,php "pruga/scripts/eval_php_ast_json.py ./php/wordpress/www.ast/index.php"

watchexec -c -w ./src/ -e py -- python src/scrapper/index.py


# while inotifywait ./src -r; do
#   if tail -n1 /var/log/messages | grep httpd; then
    echo "Apache needs love!"
#   fi
# done

# -e attrib
# inotifywait -m src/ -r -e create -e modify -e delete -e move -e attrib --exclude '__pycache__' |
#     while read path action file; do
#         clear
#         echo "$action: '$file' in directory '$path'"
#         # do something with the file
#         python src/scrapper/index.py;
#     done