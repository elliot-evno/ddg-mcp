#!/usr/bin/env python3
"""
Tests for ddg-mcp MCP Server
"""

import pytest
import asyncio
from ddg_mcp.app import example_tool, get_server_info


@pytest.mark.asyncio
async def test_example_tool():
    """Test the example tool"""
    result = await example_tool("Hello, world!")
    
    assert result["success"] is True
    assert "Hello, world!" in result["echo"]
    assert "Hello from ddg-mcp" in result["message"]


@pytest.mark.asyncio
async def test_get_server_info():
    """Test the server info tool"""
    result = await get_server_info()
    
    assert result["name"] == "ddg-mcp"
    assert result["version"] == "1.0.0"
    assert isinstance(result["tools"], list)
    assert len(result["tools"]) > 0


if __name__ == "__main__":
    pytest.main([__file__])
