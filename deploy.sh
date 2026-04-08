#!/bin/bash

# KPI Analyzer - Deployment Script
# =================================

set -e

echo "========================================="
echo "  KPI Analyzer Pro - Deployment Script  "
echo "========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | grep -oP '(?<=Python )\d+\.\d+')
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo -e "${RED}Error: Python 3.8 or higher is required${NC}"
    echo "Current version: $python_version"
    exit 1
fi

echo -e "${GREEN}✓ Python version OK: $python_version${NC}"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${YELLOW}Virtual environment already exists${NC}"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo -e "${GREEN}✓ Virtual environment activated${NC}"
echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1
echo -e "${GREEN}✓ Pip upgraded${NC}"
echo ""

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt
echo -e "${GREEN}✓ Dependencies installed${NC}"
echo ""

# Generate sample data
echo "Do you want to generate sample datasets for testing? (y/n)"
read -r generate_samples

if [ "$generate_samples" = "y" ]; then
    echo "Generating sample data..."
    python3 generate_sample_data.py
    echo -e "${GREEN}✓ Sample data generated${NC}"
    echo ""
fi

# Check port availability
echo "Checking if port 8501 is available..."
if lsof -Pi :8501 -sTCP:LISTEN -t >/dev/null ; then
    echo -e "${YELLOW}Warning: Port 8501 is already in use${NC}"
    echo "Please stop the existing service or choose a different port"
    echo ""
else
    echo -e "${GREEN}✓ Port 8501 is available${NC}"
    echo ""
fi

# Create .streamlit directory if it doesn't exist
if [ ! -d ".streamlit" ]; then
    mkdir -p .streamlit
    echo -e "${GREEN}✓ Created .streamlit directory${NC}"
fi

echo "========================================="
echo "  Deployment Complete!                   "
echo "========================================="
echo ""
echo "To start the application, run:"
echo -e "${GREEN}streamlit run kpi_analyzer_app.py${NC}"
echo ""
echo "Or use the run script:"
echo -e "${GREEN}./run.sh${NC}"
echo ""
echo "The application will be available at:"
echo -e "${GREEN}http://localhost:8501${NC}"
echo ""
echo "For production deployment with Docker:"
echo -e "${GREEN}docker build -t kpi-analyzer .${NC}"
echo -e "${GREEN}docker run -p 8501:8501 kpi-analyzer${NC}"
echo ""
