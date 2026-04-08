#!/usr/bin/env python3
"""
System Requirements Checker for KPI Analyzer
Verifies your system is ready to run the application
"""

import sys
import subprocess
import platform

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    print(f"🐍 Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("   ✅ Python version is compatible (3.8+)")
        return True
    else:
        print("   ❌ Python 3.8 or higher required")
        print("   📥 Download from: https://www.python.org/downloads/")
        return False

def check_pip():
    """Check if pip is installed"""
    try:
        result = subprocess.run(['pip', '--version'], 
                              capture_output=True, text=True, check=True)
        print(f"📦 Pip: {result.stdout.strip()}")
        print("   ✅ Pip is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("   ❌ Pip is not installed")
        print("   📥 Install pip: python -m ensurepip --upgrade")
        return False

def check_git():
    """Check if git is installed (optional)"""
    try:
        result = subprocess.run(['git', '--version'], 
                              capture_output=True, text=True, check=True)
        print(f"🔧 Git: {result.stdout.strip()}")
        print("   ✅ Git is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("   ⚠️  Git not found (optional)")
        return False

def check_docker():
    """Check if Docker is installed (optional)"""
    try:
        result = subprocess.run(['docker', '--version'], 
                              capture_output=True, text=True, check=True)
        print(f"🐳 Docker: {result.stdout.strip()}")
        print("   ✅ Docker is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("   ⚠️  Docker not found (optional, for server deployment)")
        return False

def main():
    print("=" * 60)
    print("  KPI ANALYZER PRO - SYSTEM REQUIREMENTS CHECK")
    print("=" * 60)
    print()
    
    print(f"💻 Operating System: {platform.system()} {platform.release()}")
    print(f"🖥️  Architecture: {platform.machine()}")
    print()
    
    checks = {
        'Python 3.8+': check_python_version(),
        'Pip': check_pip(),
        'Git': check_git(),
        'Docker': check_docker()
    }
    
    print()
    print("=" * 60)
    print("  SUMMARY")
    print("=" * 60)
    
    required_passed = checks['Python 3.8+'] and checks['Pip']
    
    if required_passed:
        print("✅ All required components are installed!")
        print()
        print("📝 Next steps:")
        print("   1. Download/extract the KPI Analyzer files")
        print("   2. Open terminal/command prompt")
        print("   3. Navigate to the folder: cd path/to/kpi-analyzer")
        print("   4. Run: pip install -r requirements.txt")
        print("   5. Run: streamlit run kpi_analyzer_app.py")
    else:
        print("❌ Some required components are missing")
        print()
        print("📝 Please install:")
        if not checks['Python 3.8+']:
            print("   • Python 3.8+: https://www.python.org/downloads/")
        if not checks['Pip']:
            print("   • Pip: python -m ensurepip --upgrade")
    
    print()

if __name__ == "__main__":
    main()