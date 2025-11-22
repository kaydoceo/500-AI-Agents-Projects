# 🎬 Demo Guide - Multi-Agent Team with TUI

## Quick Demo Script (5 minutes)

### 1. Introduction (30 seconds)
"Today I'll show you a multi-agent AI system with three specialized agents working together as a team."

### 2. Show the Team (30 seconds)
Run the demo and show the team table:
- **Researcher** - Gathers information
- **Writer** - Creates content
- **Reviewer** - Quality assurance

Point out: "Each agent has a specific role, goal, and tools - just like a real team."

### 3. Live Collaboration (3 minutes)
Enter a topic (suggest: "AI in Healthcare" or current trending topic)

Watch the agents work:
- **Researcher** starts first, gathering information
- **Writer** uses research to create an article
- **Reviewer** polishes the final output

Point out: "Notice how they work sequentially - each building on the previous agent's work."

### 4. Show the Result (30 seconds)
Highlight the final output panel showing the polished article.

Point out: "The final result is better than any single agent could produce alone."

### 5. Discuss Architecture (30 seconds)
Show the code briefly (main.py):
- Clean agent definitions
- Simple task orchestration
- Easy to customize and extend

## Key Talking Points

### Why Multi-Agent?
- **Specialization** - Each agent is expert in their domain
- **Collaboration** - Agents build on each other's work
- **Quality** - Multiple perspectives improve output
- **Scalability** - Easy to add more specialists

### Why This Demo?
- **Fast setup** - Minutes, not hours
- **Clean code** - Easy to understand
- **Beautiful UI** - Professional presentation
- **Extensible** - Add agents or modify tasks easily

### Technical Highlights
- **Framework**: CrewAI (purpose-built for agent teams)
- **UI Library**: Rich (beautiful terminal output)
- **Process**: Sequential (can switch to hierarchical)
- **LLM**: OpenAI GPT-4 (swappable)

## Demo Variations

### Quick Demo (2 min)
- Use default topic
- Focus on UI and real-time progress
- Show final result

### Technical Demo (10 min)
- Show code structure
- Explain agent definitions
- Discuss task orchestration
- Show how to add new agents

### Business Demo (5 min)
- Focus on use cases
- Discuss ROI and efficiency
- Show quality improvements
- Explain scalability

## Common Questions & Answers

**Q: How do you add more agents?**
A: Just define a new Agent object with role, goal, and backstory. Add it to the crew.

**Q: Can agents work in parallel?**
A: Yes! Change `Process.sequential` to `Process.hierarchical` or use async execution.

**Q: What other tasks can they do?**
A: Anything! Code review, data analysis, customer support, content creation, etc.

**Q: How much does it cost?**
A: Depends on LLM usage. This demo costs ~$0.05-0.10 per run with GPT-4.

**Q: Can I use local models?**
A: Yes! CrewAI supports any LangChain-compatible LLM (Ollama, HuggingFace, etc.)

**Q: Is it production-ready?**
A: This is a demo, but CrewAI is used in production by many companies.

## Customization Ideas for Demo

### Add a 4th Agent
```python
editor = Agent(
    role='Senior Editor',
    goal='Ensure brand consistency and tone',
    backstory='You are an experienced editor...'
)
```

### Change the Use Case
- Code Review Team (Analyzer, Tester, Reviewer)
- Customer Support Team (Researcher, Responder, Escalation Handler)
- Data Analysis Team (Collector, Analyzer, Visualizer)

### Add Real Tools
```python
from crewai_tools import SerperDevTool, WebsiteSearchTool

search_tool = SerperDevTool()
researcher = Agent(..., tools=[search_tool])
```

## Troubleshooting During Demo

### Demo runs too slow
- Switch to GPT-3.5-turbo (faster, cheaper)
- Use pre-recorded output
- Simplify task descriptions

### API errors
- Have backup API key ready
- Consider using Ollama (local) as backup
- Have screenshots of successful run

### Audience wants to try
- Have .env file pre-configured
- Quick laptop handoff ready
- Or use screen sharing for their input

## Follow-up Resources

After demo, share:
1. This GitHub repo
2. CrewAI documentation: https://docs.crewai.com
3. Your contact for questions
4. Invitation to try it themselves

## Success Metrics

A successful demo:
- ✅ Shows agent collaboration clearly
- ✅ Produces quality output
- ✅ Generates audience questions
- ✅ Runs smoothly without errors
- ✅ Inspires ideas for use cases

---

**Remember**: The goal is to inspire and educate, not to show every feature. Keep it simple and engaging!
