# Customer Accounts Microservice

A learning-oriented Flask REST API capstone starter covering account CRUD operations, automated tests, CI, security headers/CORS, Docker, Kubernetes manifests, and a Tekton pipeline example.

[![Build Status](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/actions/workflows/ci-build.yaml)

Replace `YOUR_USERNAME` and `YOUR_REPOSITORY` after publishing. The badge only becomes meaningful after the workflow runs successfully; this starter does not claim a successful build or deployment.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=service
flask run --host=0.0.0.0 --port=8080
```
Windows PowerShell: use `$env:FLASK_APP="service"` instead of `export`.

Check the service with `curl -i http://localhost:8080/` and `curl -i http://localhost:8080/accounts`.

Run checks: `nosetests`, `flake8 service tests`, `pylint service`.

See `docs/curl-examples.md` and `docs/submission-artifacts.md`.

**Important:** This is a starter project, not proof that Coursera lab tasks have been completed. Capture real Kanban screenshots, successful CI logs, Docker/Kubernetes output, and Tekton logs from your own lab environment. Do not submit placeholder evidence.
