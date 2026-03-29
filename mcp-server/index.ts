#!/usr/bin/env bun
/**
 * My MCP Server — scaffold
 *
 * This is your starting point. It creates an MCP server that responds
 * to tools/list with an empty array. Your job: design what tools it
 * should provide, then implement them.
 *
 * Run it: bun index.ts
 * Test it: bun index.ts --help
 * Register it: claude mcp add --scope project --transport stdio my-server -- bun index.ts
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

if (process.argv.includes("--help")) {
  console.log(`Usage: bun index.ts

An MCP tool server. Register with Claude Code:
  claude mcp add --scope project --transport stdio my-server -- bun index.ts

Flags:
  --help       Show this help message`);
  process.exit(0);
}

// --- Server setup ------------------------------------------------------------

const server = new Server(
  { name: "my-mcp-server", version: "0.1.0" },
  { capabilities: { tools: {} } }
);

// --- Tool definitions --------------------------------------------------------

// TODO: Define your tools here. Example:
//
// const TOOLS = [
//   {
//     name: "roll_dice",
//     description: "Roll one or more dice",
//     inputSchema: {
//       type: "object" as const,
//       properties: {
//         sides: { type: "number", description: "Number of sides per die", default: 6 },
//         count: { type: "number", description: "Number of dice to roll", default: 1 },
//       },
//     },
//   },
// ];

const TOOLS: Array<{
  name: string;
  description: string;
  inputSchema: Record<string, unknown>;
}> = [];

// --- Handlers ----------------------------------------------------------------

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: TOOLS,
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  // TODO: Handle your tools here. Example:
  //
  // if (name === "roll_dice") {
  //   const sides = (args?.sides as number) ?? 6;
  //   const count = (args?.count as number) ?? 1;
  //   const rolls = Array.from({ length: count }, () => Math.floor(Math.random() * sides) + 1);
  //   return { content: [{ type: "text", text: JSON.stringify({ rolls, total: rolls.reduce((a, b) => a + b, 0) }) }] };
  // }

  return {
    content: [{ type: "text", text: `Unknown tool: ${name}` }],
    isError: true,
  };
});

// --- Start -------------------------------------------------------------------

const transport = new StdioServerTransport();
await server.connect(transport);
