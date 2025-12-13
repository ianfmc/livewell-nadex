# nadex_common/__init__.py
"""
Nadex Common Library

Shared modules for Nadex trading strategy analysis.

Modules:
    strategy_rsi: RSI calculation and signal generation
    utils_s3: AWS S3 utilities
    kpi_calculator: KPI calculation from trades
    kpi_html_generator: HTML dashboard generation
    backtest_results: Save/load backtest results to S3
"""

# Strategy and S3 utilities
from .strategy_rsi import rsi_wilder, generate_rsi_signals
from .utils_s3 import create_s3_clients

# KPI functions
from .kpi_calculator import calculate_kpis, calculate_tier_entry_cost
from .kpi_html_generator import generate_html_dashboard, get_template_path

# Backtest results persistence
from .backtest_results import BacktestResults, load_backtest_schema

__all__ = [
    # Strategy
    'rsi_wilder',
    'generate_rsi_signals',
    
    # S3
    'create_s3_clients',
    
    # KPI
    'calculate_kpis',
    'calculate_tier_entry_cost',
    'generate_html_dashboard',
    'get_template_path',
    
    # Backtest Results
    'BacktestResults',
    'load_backtest_schema',
]
