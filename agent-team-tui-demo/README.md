# 🤖 Multi-Agent Team Demo with TUI Interface

A fast and clean demonstration of collaborative AI agents with a beautiful Terminal User Interface (TUI).

## ✨ Features

- **3 Specialized Agents:**
  - 📊 **Researcher** - Gathers comprehensive information
  - ✍️ **Writer** - Creates engaging content
  - 🔍 **Reviewer** - Ensures quality and accuracy

- **Beautiful TUI** - Clean terminal interface using Rich library
- **Fast Setup** - Ready to demo in minutes
- **Team Collaboration** - Agents work together sequentially
- **Real-time Progress** - Watch agents collaborate in real-time

## 🎯 Demo Showcase

The team collaborates to research and write about any topic you choose:
1. Researcher gathers information
2. Writer crafts an article
3. Reviewer polishes the final output

Perfect for demonstrating multi-agent AI systems!

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- OpenAI API key

### Installation

```bash
# Clone or navigate to the demo directory
cd agent-team-tui-demo

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project directory:

```bash
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

Or export it directly:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

### Run the Demo

```bash
python main.py
```

## 📖 Usage

1. Run the script
2. Enter a topic when prompted (or use the default)
3. Watch the agents collaborate!
4. See the final polished article

### Example Topics

- "Artificial Intelligence in Healthcare"
- "Future of Quantum Computing"
- "Sustainable Energy Solutions"
- "Space Exploration Technologies"
- "Blockchain and Web3"

## 🎨 TUI Features

- **Color-coded output** - Easy to follow agent activities
- **Progress indicators** - Real-time status updates
- **Formatted results** - Beautiful panels and tables
- **Status tracking** - See each agent's current task

## 🏗️ Architecture

```
agent-team-tui-demo/
├── main.py              # Main application with TUI
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── .env                # API keys (create this)
```

## 🔧 Customization

### Add More Agents

Edit `create_research_team()` in `main.py`:

```python
new_agent = Agent(
    role='Your Role',
    goal='Your Goal',
    backstory='Your Backstory',
    verbose=True
)
```

### Modify Tasks

Update task descriptions in `run_team_demo()`:

```python
custom_task = Task(
    description="Your custom task description",
    expected_output="Expected output format",
    agent=your_agent
)
```

### Change Team Process

In the `Crew` initialization, switch between:
- `Process.sequential` - One after another
- `Process.hierarchical` - Manager-based delegation

## 💡 Tips for Demo

1. **Start Simple** - Use default topics first
2. **Show the Code** - Display the clean agent definitions
3. **Highlight Collaboration** - Point out how agents build on each other's work
4. **Explain the TUI** - Show the real-time progress indicators
5. **Discuss Scalability** - Mention how easy it is to add more agents

## 🐛 Troubleshooting

### "API Key Not Found"
- Make sure `.env` file exists with `OPENAI_API_KEY`
- Or set environment variable: `export OPENAI_API_KEY="your-key"`

### "Module Not Found"
- Activate virtual environment: `source venv/bin/activate`
- Reinstall dependencies: `pip install -r requirements.txt`

### Slow Performance
- Use GPT-3.5-turbo for faster demos (edit agent model in code)
- Reduce task complexity

## 📚 Learn More

- [CrewAI Documentation](https://docs.crewai.com)
- [Rich Library](https://rich.readthedocs.io)
- [Multi-Agent Systems](https://github.com/ashishpatel26/500-AI-Agents-Projects)

## 🎯 Use Cases

This demo is perfect for:
- **Team presentations** - Show AI agent collaboration
- **Educational purposes** - Teach multi-agent concepts
- **Proof of concept** - Demonstrate agent orchestration
- **Client demos** - Quick, impressive visualization

## 📝 License

MIT License - Feel free to use and modify!

## 🌟 What's Next?

- Add more specialized agents
- Implement parallel processing
- Add agent memory and context
- Create different team compositions
- Build domain-specific teams

---

**Made with ❤️ using CrewAI and Rich**
