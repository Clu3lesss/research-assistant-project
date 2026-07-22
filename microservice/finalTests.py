import main

agent = main.research_project()
response = agent.invoke({
    "messages": [{"role": "user", "content": "What experimental results does this paper present about laser wake field acceleration?"}]
})

print(response["messages"][-1].content)