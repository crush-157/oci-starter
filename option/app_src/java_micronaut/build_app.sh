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
. $SCRIPT_DIR/../bin/build_common.sh
check_java_version

if [ "$TF_VAR_java_vm" == "graalvm_native" ]; then
  mvn package -Dpackaging=native-image
else 
  mvn package 
fi

if [ "$TF_VAR_deploy_strategy" == "compute" ]; then
  # Replace the user and password
  cp start.sh target/.
  sed -i "s/##DB_USER##/$TF_VAR_db_user/" target/start.sh
  sed -i "s/##DB_PASSWORD##/$TF_VAR_db_password/" target/start.sh

  mkdir ../compute/app
  cp -r target/* ../compute/app/.

elif [ "$TF_VAR_deploy_strategy" == "kubernetes" ]; then
  docker image rm app:latest
  docker build -t app:latest .

  if [ "$TF_VAR_java_vm" == "graalvm_native" ]; then
    docker build -f Dockerfile.native -t app:latest .
  else
    docker build -t app:latest . 
  fi  
fi  