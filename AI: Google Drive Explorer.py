# This is a code export from Open AI's agent builder 
# This program connects to Google Drive and has access to the files within it and can be prompted to respond to questions using thos files
# I am using a Google sheets file with mock vehicle data as a reference for the program to answer automotive questions

import { hostedMcpTool, Agent, AgentInputItem, Runner, withTrace } from "@openai/agents";


// Tool definitions
const mcp = hostedMcpTool({
  serverLabel: "googledrive",
  allowedTools: [
    "fetch",
    "get_profile",
    "list_drives",
    "recent_documents",
    "search"
  ],
  authorization: XXXXXXX
  connectorId: "connector_googledrive",
  requireApproval: "never"
})
const databaseInformer = new Agent({
  name: "Database Informer",
  instructions: "Search for a file called \"CRM Mock Data\" in the Google Drive and answer all of the user's questions about its contents.",
  model: "gpt-5-nano",
  tools: [
    mcp
  ],
  modelSettings: {
    reasoning: {
      effort: "medium"
    },
    store: true
  }
});

type WorkflowInput = { input_as_text: string };


// Main code entrypoint
export const runWorkflow = async (workflow: WorkflowInput) => {
  return await withTrace("Google Drive Explorer", async () => {
    const state = {

    };
    const conversationHistory: AgentInputItem[] = [
      {
        role: "user",
        content: [
          {
            type: "input_text",
            text: workflow.input_as_text
          }
        ]
      }
    ];
    const runner = new Runner({
      traceMetadata: {
        __trace_source__: "agent-builder",
        workflow_id: "wf_690b9ebfbab081908563bf5aa69aeba00890d07ea4d55186"
      }
    });
    const databaseInformerResultTemp = await runner.run(
      databaseInformer,
      [
        ...conversationHistory
      ]
    );
    conversationHistory.push(...databaseInformerResultTemp.newItems.map((item) => item.rawItem));

    if (!databaseInformerResultTemp.finalOutput) {
        throw new Error("Agent result is undefined");
    }

    const databaseInformerResult = {
      output_text: databaseInformerResultTemp.finalOutput ?? ""
    };
  });
}
