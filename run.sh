#!/bin/bash

# KPI Analyzer - Run Script
# ==========================

echo "Starting KPI Analyzer Pro..."
echo ""

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✓ Virtual environment activated"
fi

# Start Streamlit
echo "Launching application on http://localhost:8501"
echo ""
streamlit run kpi_analyzer_app.py
