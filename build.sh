#!/usr/bin/env bash
# build.sh

# Set production environment
export RENDER=true
export DJANGO_SETTINGS_MODULE=config-admin.settings_render

# Install system dependencies
apt-get update
apt-get install -y postgresql-client libpq-dev

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run database migrations
python manage.py migrate --settings=config-admin.settings_render

# Collect static files
python manage.py collectstatic --noinput --settings=config-admin.settings_render

echo "✅ Build completed successfully!"
