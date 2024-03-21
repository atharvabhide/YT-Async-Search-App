#!/bin/bash
modes="start-dev stop-dev interactive-dev check-syntax"
mode=$1
project_name="ytasyncsearch"

if [ "$project_name" == "*****" ]; then
    echo "Please Update the Project Name in run.sh"
    exit 0;
fi

if [ "$mode" == "" ]; then
    echo "Invalid mode.\n mode must be one of: ${modes}"
elif [ "$mode" == "start-dev" ]; then
    docker-compose -p ${project_name} -f docker-compose.yml build
    docker-compose -p ${project_name} -f docker-compose.yml up -d
    docker exec -it --user root ${project_name}-backend python manage.py migrate
elif [ "$mode" == "stop-dev" ]; then
    docker-compose -p ${project_name} -f docker-compose.yml down
elif [ "$mode" == "interactive-dev" ]; then
    docker exec -it --user root ${project_name}-backend bash
elif [ "$mode" == "check-syntax" ]; then
    docker exec -it --user root ${project_name}-backend flake8 .
else
    echo "Invalid mode.\n mode must be one of: ${modes}"
fi