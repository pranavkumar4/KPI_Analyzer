# 🚀 Quick Start Guide - KPI Analyzer Pro

## ⚡ 5-Minute Setup

### Option 1: Streamlit (Fastest)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
streamlit run kpi_analyzer_app.py

# 3. Open browser
# http://localhost:8501
```

### Option 2: Docker (Production)

```bash
# 1. Build image
docker build -t kpi-analyzer .

# 2. Run container
docker run -p 8501:8501 kpi-analyzer

# 3. Open browser
# http://localhost:8501
```

### Option 3: Automated Setup

```bash
# Make script executable
chmod +x deploy.sh

# Run deployment
./deploy.sh

# Start application
./run.sh
```

---

## 📝 First Use

1. **Upload Data**
   - Click "Browse file" in sidebar
   - Select your CSV/Excel file
   - Wait for processing

2. **Explore Results**
   - Tab 1: Data Profile
   - Tab 2: KPI Dictionary
   - Tab 3: Dashboard
   - Tab 4: Advanced Analytics
   - Tab 5: Export

3. **Download Report**
   - Go to Export tab
   - Click "Generate Excel Export"
   - Download your results

---

## 🧪 Test with Sample Data

```bash
# Generate sample datasets
python generate_sample_data.py

# This creates:
# - sample_claims_data.xlsx
# - sample_sales_data.xlsx
# - sample_financial_data.xlsx
```

---

## 📚 Full Documentation

- **README.md** - Complete technical documentation
- **USER_GUIDE.md** - Detailed usage instructions
- **Requirements.txt** - Python dependencies
- **Dockerfile** - Container configuration
- **docker-compose.yml** - Multi-container setup

---

## 🆘 Need Help?

**Common Issues:**

1. **Port 8501 already in use**
   ```bash
   streamlit run kpi_analyzer_app.py --server.port 8502
   ```

2. **Module not found**
   ```bash
   pip install -r requirements.txt
   ```

3. **Permission denied**
   ```bash
   chmod +x deploy.sh run.sh
   ```

---

## ✅ Checklist

- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Application running (`streamlit run kpi_analyzer_app.py`)
- [ ] Browser opened to http://localhost:8501
- [ ] Sample data generated (optional)

---

## 🎯 What You Get

✅ **Intelligent KPI Detection**  
✅ **Data Quality Assessment**  
✅ **Interactive Dashboards**  
✅ **Excel Reports**  
✅ **Production Ready**

---

**Ready to analyze? Start the app and upload your data!** 🚀
