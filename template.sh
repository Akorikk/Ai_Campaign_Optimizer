#!/bin/bash

echo "Creating AI Recruiting Campaign Optimizer project structure..."

# Root folders
mkdir -p backend/api
mkdir -p backend/core
mkdir -p backend/models
mkdir -p backend/services
mkdir -p backend/schemas

mkdir -p frontend
mkdir -p data
mkdir -p ml_models
mkdir -p notebooks
mkdir -p tests
mkdir -p docker
mkdir -p scripts

# Backend files
touch backend/main.py

touch backend/api/campaign_routes.py
touch backend/api/recommendation_routes.py
touch backend/api/candidate_routes.py
touch backend/api/analytics_routes.py

touch backend/core/config.py
touch backend/core/database.py

touch backend/models/campaign.py
touch backend/models/candidate.py

touch backend/services/channel_recommendation.py
touch backend/services/resume_ranker.py
touch backend/services/analytics_service.py

touch backend/schemas/campaign_schema.py
touch backend/schemas/candidate_schema.py

# Frontend
touch frontend/streamlit_app.py

# ML models
touch ml_models/train_channel_model.py

# Tests
touch tests/test_api.py

# Docker
touch docker/Dockerfile

# Scripts
touch scripts/run_server.sh

# Root files
touch requirements.txt
touch README.md
touch .env

echo "Project structure created successfully!"