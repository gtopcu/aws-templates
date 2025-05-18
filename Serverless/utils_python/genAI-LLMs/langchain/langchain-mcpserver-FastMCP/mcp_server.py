
# https://www.youtube.com/watch?v=3K39NJbp2IA
# pip install -U yfinance asyncio langchain-mcp-adapters langchain-openai langgraph fastmcp

from fastmcp import FastMCP
from pandas import DataFrame

import yfinance as yf

mcp = FastMCP("stocks")

@mcp.tool()
def fetch_stock_info(symbol: str) -> dict:
    """Get general info about the company"""
    stock = yf.Ticker(symbol)
    return stock.info

@mcp.tool()
def fetch_quarterly_financials(symbol: str) -> DataFrame:
    """Get stock quarterly financials"""
    stock = yf.Ticker(symbol)
    return stock.quarterly_financials.T

@mcp.tool()
def fetch_annual_financials(symbol: str) -> DataFrame:
    """Get stock yearly financials"""
    stock = yf.Ticker(symbol)
    return stock.financials.T

if __name__ == "__main__":
    mcp.run(transport="stdio")
