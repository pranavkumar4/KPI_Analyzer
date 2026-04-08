"""
Sample Data Generator for KPI Analyzer Testing
==============================================
Generates realistic sample datasets for testing the KPI Analyzer application.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_claims_data(n_rows=1000):
    """Generate sample healthcare claims data"""
    
    np.random.seed(42)
    random.seed(42)
    
    # Date range
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    date_range = (end_date - start_date).days
    
    # Status options
    statuses = ['paid', 'pending', 'denied', 'void']
    status_weights = [0.7, 0.15, 0.1, 0.05]
    
    # Network options
    networks = ['In-Network', 'Out-of-Network']
    network_weights = [0.8, 0.2]
    
    # Generate data
    data = {
        'claim_id': [f'CLM{str(i).zfill(6)}' for i in range(1, n_rows + 1)],
        'member_id': [f'MEM{random.randint(1000, 9999)}' for _ in range(n_rows)],
        'provider_id': [f'PRV{random.randint(100, 999)}' for _ in range(n_rows)],
        'provider_name': [f'Provider {random.choice(["A", "B", "C", "D", "E", "F"])}' for _ in range(n_rows)],
        'diagnosis_code': [f'I{random.randint(10, 99)}.{random.randint(0, 9)}' for _ in range(n_rows)],
        'procedure_code': [f'{random.randint(10000, 99999)}' for _ in range(n_rows)],
        'service_date': [start_date + timedelta(days=random.randint(0, date_range)) for _ in range(n_rows)],
        'paid_date': [start_date + timedelta(days=random.randint(0, date_range)) for _ in range(n_rows)],
        'charge_amount': np.random.lognormal(7, 1, n_rows).round(2),
        'allowed_amount': None,  # Will calculate based on charge
        'paid_amount': None,  # Will calculate based on allowed
        'status': random.choices(statuses, weights=status_weights, k=n_rows),
        'network': random.choices(networks, weights=network_weights, k=n_rows),
        'plan_name': [f'Plan {random.choice(["Gold", "Silver", "Bronze"])}' for _ in range(n_rows)],
        'member_state': [random.choice(['CA', 'NY', 'TX', 'FL', 'IL']) for _ in range(n_rows)]
    }
    
    df = pd.DataFrame(data)
    
    # Calculate allowed amount (80-95% of charge)
    df['allowed_amount'] = (df['charge_amount'] * np.random.uniform(0.8, 0.95, n_rows)).round(2)
    
    # Calculate paid amount based on status
    df['paid_amount'] = df.apply(lambda row: 
        0 if row['status'] in ['denied', 'void', 'pending']
        else (row['allowed_amount'] * np.random.uniform(0.8, 1.0)).round(2),
        axis=1
    )
    
    # Add some missing values (5%)
    missing_mask = np.random.random(n_rows) < 0.05
    df.loc[missing_mask, 'diagnosis_code'] = None
    
    return df


def generate_sales_data(n_rows=1000):
    """Generate sample sales data"""
    
    np.random.seed(42)
    random.seed(42)
    
    # Date range
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    date_range = (end_date - start_date).days
    
    # Product categories
    categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books']
    regions = ['North', 'South', 'East', 'West', 'Central']
    
    data = {
        'transaction_id': [f'TXN{str(i).zfill(6)}' for i in range(1, n_rows + 1)],
        'customer_id': [f'CUST{random.randint(1000, 5000)}' for _ in range(n_rows)],
        'transaction_date': [start_date + timedelta(days=random.randint(0, date_range)) for _ in range(n_rows)],
        'product_category': [random.choice(categories) for _ in range(n_rows)],
        'product_name': [f'Product {random.randint(1, 100)}' for _ in range(n_rows)],
        'quantity': np.random.randint(1, 10, n_rows),
        'unit_price': np.random.uniform(10, 500, n_rows).round(2),
        'total_revenue': None,  # Will calculate
        'cost_of_goods': None,  # Will calculate
        'profit': None,  # Will calculate
        'region': [random.choice(regions) for _ in range(n_rows)],
        'sales_channel': [random.choice(['Online', 'In-Store', 'Phone']) for _ in range(n_rows)],
        'customer_segment': [random.choice(['Retail', 'Wholesale', 'Enterprise']) for _ in range(n_rows)]
    }
    
    df = pd.DataFrame(data)
    
    # Calculate revenue
    df['total_revenue'] = (df['quantity'] * df['unit_price']).round(2)
    
    # Calculate cost (60-80% of revenue)
    df['cost_of_goods'] = (df['total_revenue'] * np.random.uniform(0.6, 0.8, n_rows)).round(2)
    
    # Calculate profit
    df['profit'] = (df['total_revenue'] - df['cost_of_goods']).round(2)
    
    # Add some missing values
    missing_mask = np.random.random(n_rows) < 0.03
    df.loc[missing_mask, 'customer_segment'] = None
    
    return df


def generate_financial_data(n_rows=500):
    """Generate sample financial data"""
    
    np.random.seed(42)
    
    # Generate monthly data for 2 years
    months = pd.date_range(start='2023-01', end='2024-12', freq='MS')
    departments = ['Sales', 'Marketing', 'Operations', 'IT', 'HR', 'Finance']
    
    data = []
    for month in months:
        for dept in departments:
            data.append({
                'period': month,
                'department': dept,
                'revenue': np.random.uniform(100000, 500000),
                'expenses': np.random.uniform(50000, 300000),
                'headcount': np.random.randint(10, 100),
                'budget': np.random.uniform(80000, 350000),
                'actual_spend': np.random.uniform(70000, 400000)
            })
    
    df = pd.DataFrame(data)
    
    # Calculate derived metrics
    df['profit'] = df['revenue'] - df['expenses']
    df['profit_margin'] = (df['profit'] / df['revenue'] * 100).round(2)
    df['budget_variance'] = ((df['actual_spend'] - df['budget']) / df['budget'] * 100).round(2)
    
    # Round numeric columns
    for col in ['revenue', 'expenses', 'budget', 'actual_spend', 'profit']:
        df[col] = df[col].round(2)
    
    return df


if __name__ == "__main__":
    """Generate sample datasets"""
    
    print("Generating sample datasets...")
    
    # Generate claims data
    print("\n1. Generating claims data...")
    claims_df = generate_claims_data(1000)
    claims_df.to_csv('sample_claims_data.csv', index=False)
    claims_df.to_excel('sample_claims_data.xlsx', index=False)
    print(f"   ✓ Generated {len(claims_df)} claims records")
    print(f"   ✓ Saved to sample_claims_data.csv and .xlsx")
    
    # Generate sales data
    print("\n2. Generating sales data...")
    sales_df = generate_sales_data(1000)
    sales_df.to_csv('sample_sales_data.csv', index=False)
    sales_df.to_excel('sample_sales_data.xlsx', index=False)
    print(f"   ✓ Generated {len(sales_df)} sales records")
    print(f"   ✓ Saved to sample_sales_data.csv and .xlsx")
    
    # Generate financial data
    print("\n3. Generating financial data...")
    financial_df = generate_financial_data()
    financial_df.to_csv('sample_financial_data.csv', index=False)
    financial_df.to_excel('sample_financial_data.xlsx', index=False)
    print(f"   ✓ Generated {len(financial_df)} financial records")
    print(f"   ✓ Saved to sample_financial_data.csv and .xlsx")
    
    print("\n✅ All sample datasets generated successfully!")
    print("\nYou can now test the KPI Analyzer with these files:")
    print("  • sample_claims_data.xlsx - Healthcare claims")
    print("  • sample_sales_data.xlsx - Sales transactions")
    print("  • sample_financial_data.xlsx - Financial metrics")
