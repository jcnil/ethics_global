#! /bin/sh
# -----------------------> RUN WITH sudo <------------------------------------------
# Remove previous flake file if already exist
rm flake8.txt
# Run Flake 8
# flake8 --exclude .git,__pycache__,venv/ > flake8.txt
flake8 --exclude venv/ --ignore=W291 --output-file flake8.txt  --max-line-length 120
sleep 2

# run docker
docker start sonarqube
sleep 40
# Sonar-scanner
PROJECT_NAME="fast-api-base"
PROJECT_KEY="59534664e3839462675173f406f11a2e1de3e8d9"
sonar-scanner \
  -Dsonar.python.flake8.reportPaths=flake8.txt\
  -Dsonar.projectKey=$PROJECT_NAME \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://0.0.0.0:9000 \
  -Dsonar.login=$PROJECT_KEY

