# 📊 KPI Analyzer Pro

A production-grade Python application for intelligent KPI detection, data profiling, and interactive analytics dashboards.

## 🌟 Features

### Core Capabilities
- **🎯 Intelligent KPI Detection** - Automatically identifies KPIs using pattern matching and heuristics
- **📋 Data Profiling** - Comprehensive data quality assessment and statistics
- **🧹 Data Cleaning** - Automatic data cleaning and type conversion
- **📊 Interactive Dashboard** - Real-time visualizations with Plotly
- **📈 Advanced Analytics** - Correlation analysis, time series, distributions
- **💾 Excel Export** - Professional multi-sheet reports
- **🚀 Production-Ready** - Scalable, efficient, and user-friendly

### KPI Categories Detected
- **Direct Measures** - Revenue, costs, volumes from columns
- **Derived Metrics** - Profit margins, ratios, growth rates
- **Temporal KPIs** - Monthly trends, period-over-period analysis
- **Aggregate KPIs** - Totals, averages, statistical summaries

## 🏗️ Architecture

```
kpi_analyzer_app.py
├── DataProfiler       # Data quality assessment
├── KPIDetector        # Intelligent KPI extraction
├── DataCleaner        # Data cleaning & transformation
├── DashboardVisualizer # Interactive charts
└── Export Functions   # Excel generation
```

## 🚀 Quick Start

### Option 1: Local Installation (Streamlit)

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Run the Application**
```bash
streamlit run kpi_analyzer_app.py
```

3. **Access the Application**
```
Open browser: http://localhost:8501
```

### Option 2: Docker Deployment

1. **Build Docker Image**
```bash
docker build -t kpi-analyzer .
```

2. **Run Container**
```bash
docker run -p 8501:8501 kpi-analyzer
```

3. **Access the Application**
```
Open browser: http://localhost:8501
```

### Option 3: Docker Compose (Recommended for Production)

1. **Create docker-compose.yml**
```yaml
version: '3.8'

services:
  kpi-analyzer:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
    environment:
      - STREAMLIT_SERVER_MAX_UPLOAD_SIZE=200
    restart: unless-stopped
```

2. **Deploy**
```bash
docker-compose up -d
```

## 📖 Usage Guide

### Step 1: Upload Data
- Click **"Browse file"** in the sidebar
- Select CSV or Excel file (max 200MB recommended)
- Supported formats: `.csv`, `.xlsx`, `.xls`

### Step 2: Review Data Profile
Navigate to **"📋 Data Profile"** tab to see:
- Data quality score
- Column types and statistics
- Missing value analysis
- Data cleaning operations performed

### Step 3: Explore KPI Dictionary
Navigate to **"🎯 KPI Dictionary"** tab to:
- View all detected KPIs
- Filter by category or type
- See definitions and formulas
- Review source columns

### Step 4: Analyze Dashboard
Navigate to **"📊 Dashboard"** tab for:
- Key metric cards
- Time series analysis
- Distribution charts
- Top categories breakdown

### Step 5: Advanced Analytics
Navigate to **"📈 Advanced Analytics"** tab for:
- Correlation heatmap
- Statistical summaries
- Data sampling and exploration

### Step 6: Export Results
Navigate to **"💾 Export"** tab to:
- Generate Excel report
- Download comprehensive analysis
- Share with stakeholders

## 📊 Sample Data Format

Your dataset can include any of these column types (automatically detected):

```csv
claim_id, member_id, service_date, paid_amount, charge_amount, status, provider_name
C001, M123, 2024-01-15, 1500.00, 2000.00, paid, Dr. Smith
C002, M124, 2024-01-16, 800.00, 1000.00, pending, Dr. Jones
...
```

The application intelligently detects:
- **Revenue/Cost columns**: revenue, sales, cost, expense, paid, charged
- **Volume columns**: quantity, count, volume, units
- **Date columns**: date, time, period, month, year
- **Category columns**: status, type, category, region, product
- **ID columns**: id, code, number, identifier

## 🔧 Configuration

### Environment Variables

Create `.env` file:
```bash
# Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_MAX_UPLOAD_SIZE=200

# Data Processing
MAX_ROWS=200000
CHUNK_SIZE=10000
```

### Custom Configuration

Modify constants in `kpi_analyzer_app.py`:

```python
# Maximum file size (bytes)
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB

# Maximum rows to process
MAX_ROWS = 200000

# KPI detection patterns
FIELD_PATTERNS = {
    'revenue': ['revenue', 'sales', 'income'],
    'cost': ['cost', 'expense', 'spend'],
    # Add custom patterns
}
```

## 🎨 Customization

### Adding Custom KPI Detection Logic

Extend the `KPIDetector` class:

```python
def _detect_custom_kpis(self):
    """Add your custom KPI detection logic"""
    
    # Example: Detect churn rate
    if 'customer_status' in self.df.columns:
        churned = self.df[self.df['customer_status'] == 'churned']
        churn_rate = len(churned) / len(self.df) * 100
        
        kpi = {
            'name': 'Customer Churn Rate',
            'definition': 'Percentage of customers who left',
            'formula': 'COUNT(churned) / COUNT(total) * 100',
            'category': 'Retention',
            'data_type': 'Percentage',
            'source_column': 'customer_status',
            'kpi_type': 'Derived Metric',
            'calculation': lambda df: churn_rate
        }
        self.kpi_dictionary.append(kpi)
```

### Adding Custom Visualizations

Extend the `DashboardVisualizer` class:

```python
@staticmethod
def create_custom_chart(df: pd.DataFrame) -> go.Figure:
    """Add your custom visualization"""
    
    fig = go.Figure()
    # Your custom Plotly code
    return fig
```

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.32.0 | Web application framework |
| pandas | 2.2.0 | Data manipulation |
| numpy | 1.26.4 | Numerical computing |
| plotly | 5.19.0 | Interactive visualizations |
| openpyxl | 3.1.2 | Excel file handling |
| xlrd | 2.0.1 | Excel file reading |

## 🔒 Security Considerations

### Data Privacy
- All data processing is done in-memory
- No data is stored persistently by default
- Files are processed and discarded after session

### Production Deployment
- Use HTTPS in production
- Implement authentication (e.g., Streamlit Auth)
- Set upload size limits
- Configure CORS policies
- Use environment variables for secrets

### Recommended Security Headers

Add to Streamlit config (`.streamlit/config.toml`):

```toml
[server]
enableCORS = false
enableXsrfProtection = true
maxUploadSize = 200

[browser]
gatherUsageStats = false
```

## 🚀 Production Deployment

### AWS EC2 Deployment

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install python3-pip

# Clone repository
git clone <your-repo>
cd kpi-analyzer

# Install requirements
pip3 install -r requirements.txt

# Run with nohup
nohup streamlit run kpi_analyzer_app.py --server.port 8501 &
```

### Azure App Service

1. Create `startup.sh`:
```bash
#!/bin/bash
python -m streamlit run kpi_analyzer_app.py --server.port 8000 --server.address 0.0.0.0
```

2. Deploy using Azure CLI:
```bash
az webapp up --name kpi-analyzer --resource-group myResourceGroup
```

### Heroku Deployment

1. Create `Procfile`:
```
web: streamlit run kpi_analyzer_app.py --server.port $PORT
```

2. Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
```

3. Deploy:
```bash
heroku create kpi-analyzer
git push heroku main
```

## 🧪 Testing

### Unit Tests (Optional Enhancement)

Create `test_kpi_analyzer.py`:

```python
import unittest
import pandas as pd
from kpi_analyzer_app import DataProfiler, KPIDetector, DataCleaner

class TestDataProfiler(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'revenue': [100, 200, 300],
            'cost': [50, 100, 150]
        })
    
    def test_profile_generation(self):
        profiler = DataProfiler(self.df)
        profile = profiler.generate_profile()
        self.assertIsNotNone(profile)
        self.assertEqual(profile['shape'], (3, 2))

if __name__ == '__main__':
    unittest.run()
```

## 📊 Performance Optimization

### For Large Datasets

1. **Use Chunking**
```python
chunk_size = 10000
chunks = pd.read_csv('large_file.csv', chunksize=chunk_size)
for chunk in chunks:
    process_chunk(chunk)
```

2. **Enable Caching**
```python
@st.cache_data
def load_data(file):
    return pd.read_csv(file)
```

3. **Use Parquet Format**
```python
# Convert CSV to Parquet for faster loading
df.to_parquet('data.parquet')
df = pd.read_parquet('data.parquet')
```

## 🐛 Troubleshooting

### Common Issues

**Issue: "File too large" error**
```bash
# Increase max upload size
streamlit run app.py --server.maxUploadSize 500
```

**Issue: Memory error with large files**
```python
# Use dtype specification to reduce memory
df = pd.read_csv('file.csv', dtype={'id': 'int32'})
```

**Issue: Slow visualization rendering**
```python
# Reduce data points for visualization
df_sample = df.sample(1000)  # Use sample for charts
```

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🎓 Credits

Built with:
- [Streamlit](https://streamlit.io/) - App framework
- [Plotly](https://plotly.com/) - Visualizations
- [Pandas](https://pandas.pydata.org/) - Data processing

## 📧 Support

For issues and questions:
- Create an issue on GitHub
- Email: support@example.com
- Documentation: [Wiki](wiki-link)

## 🗺️ Roadmap

Future enhancements:
- [ ] NLP-based KPI definition generation using LLMs
- [ ] Multi-tenancy support with user authentication
- [ ] Role-based access control (admin/user)
- [ ] Database integration for persistent storage
- [ ] Scheduled report generation
- [ ] Email notifications
- [ ] API endpoints for integration
- [ ] Real-time data streaming support
- [ ] Custom KPI formula builder
- [ ] Collaborative features

---

**Version:** 1.0.0  
**Last Updated:** April 2026  
**Status:** Production Ready ✅
