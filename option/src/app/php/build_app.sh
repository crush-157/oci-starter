#!/bin/bash
# Build_app.sh
#
# Compute:
# - build the code 
# - create a $ROOT/compute/app directory with the compiled files
# - and a start.sh to start the program
# Docker:
# - build the image
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
. $SCRIPT_DIR/../../bin/build_common.sh

## XXXXX Check Language version

if [ "$TF_VAR_deploy_strategy" == "compute" ]; then
  mkdir -p ../../target/compute/app
  cp -r src/* ../../target/compute/app/.
  # Replace the user and password in the start file
  replace_db_user_password_in_file ../../target/compute/app/php.ini.append
else
  docker image rm app:latest
  docker build -t app:latest .
  exit_on_error
fi  
