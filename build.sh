#!/usr/bin/env bash
# build.sh

# Install system dependencies
apt-get update
apt-get install -y postgresql-client libpq-dev

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput --settings=config-admin.settings_production
