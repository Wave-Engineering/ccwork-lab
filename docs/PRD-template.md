# PRD: [Your MCP Server Name]

## Summary

[One paragraph: what this MCP server does, who it's for, and why it's useful]

## Tools

For each tool, define:

### Tool: `tool_name`
- **Description:** What it does (this is shown to Claude)
- **Parameters:**
  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | param1 | string | yes | What it means |
  | param2 | number | no | What it means |
- **Returns:** What the tool returns (format and content)
- **Example:** A concrete example of input → output
- **Error cases:** What can go wrong and how it's reported

### Tool: `another_tool`
...

## Resources (optional)

MCP resources expose read-only data. If your server has any:

### Resource: `resource://name`
- **Description:** What data it exposes
- **MIME type:** `application/json` (or other)

## Configuration

How is the server configured?
- Environment variables? Config file? Command-line flags?
- What's required vs optional?
- Sensible defaults?

## Test Plan

### Unit Tests
| Test | What it verifies |
|------|-----------------|
| `test_tool_name_basic` | Tool returns expected output for standard input |
| `test_tool_name_error` | Tool handles invalid input gracefully |

### Integration Tests
| Test | What it verifies |
|------|-----------------|
| `test_server_starts` | Server initializes and responds to tools/list |
| `test_tool_roundtrip` | Tool can be called via MCP protocol and returns valid response |

## Success Metrics

- [ ] All tools respond correctly when called by Claude in a live session
- [ ] Server starts in under 2 seconds
- [ ] No unhandled exceptions on malformed input
- [ ] `claude mcp list` shows the server registered
