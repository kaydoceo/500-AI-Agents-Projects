#!/usr/bin/env python3
"""
Multi-Agent Team Demo with TUI Interface
A clean and fast demo showcasing collaborative AI agents with terminal UI
"""

import os
from crewai import Agent, Task, Crew, Process
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.layout import Layout
from rich.text import Text
from rich.prompt import Prompt
from rich import box
import time

# Initialize Rich console
console = Console()


class AgentTeamTUI:
    """Terminal UI for Multi-Agent Team"""

    def __init__(self):
        self.console = Console()

    def display_banner(self):
        """Display welcome banner"""
        banner = """
        ╔══════════════════════════════════════════════════╗
        ║     🤖 MULTI-AGENT TEAM DEMO 🤖                 ║
        ║     Fast & Clean Team Collaboration              ║
        ╚══════════════════════════════════════════════════╝
        """
        self.console.print(Panel(banner, style="bold blue", border_style="cyan"))

    def display_team_info(self):
        """Display team member information"""
        table = Table(title="🎯 Agent Team Members", box=box.ROUNDED, style="cyan")
        table.add_column("Role", style="bold yellow", no_wrap=True)
        table.add_column("Goal", style="green")
        table.add_column("Tools", style="magenta")

        table.add_row(
            "📊 Researcher",
            "Gather comprehensive information",
            "Web Search, Analysis"
        )
        table.add_row(
            "✍️ Writer",
            "Create engaging content",
            "Content Creation, Editing"
        )
        table.add_row(
            "🔍 Reviewer",
            "Quality assurance & validation",
            "Review, Feedback"
        )

        self.console.print(table)
        self.console.print()

    def display_progress(self, agent_name: str, task: str, status: str = "working"):
        """Display real-time agent progress"""
        emoji = "🔄" if status == "working" else "✅" if status == "done" else "⚠️"
        self.console.print(
            f"{emoji} [bold cyan]{agent_name}[/bold cyan]: {task}",
            style="dim" if status == "done" else ""
        )

    def display_result(self, result: str):
        """Display final result in a panel"""
        self.console.print()
        self.console.print(Panel(
            result,
            title="[bold green]✨ Final Result ✨[/bold green]",
            border_style="green",
            padding=(1, 2)
        ))


def create_research_team():
    """Create a collaborative research team"""

    # Define Agents
    researcher = Agent(
        role='Senior Research Analyst',
        goal='Uncover cutting-edge developments and insights',
        backstory="""You are an expert research analyst with a keen eye for detail.
        You excel at gathering comprehensive information from multiple sources
        and synthesizing complex data into clear insights.""",
        verbose=True,
        allow_delegation=True
    )

    writer = Agent(
        role='Content Writer',
        goal='Craft compelling and engaging content from research findings',
        backstory="""You are a talented writer who can transform complex research
        into clear, engaging narratives. Your writing is informative yet accessible,
        perfect for a broad audience.""",
        verbose=True,
        allow_delegation=False
    )

    reviewer = Agent(
        role='Quality Reviewer',
        goal='Ensure content accuracy, clarity, and impact',
        backstory="""You are a meticulous reviewer with high standards.
        You catch errors, improve clarity, and ensure every piece of content
        meets the highest quality standards.""",
        verbose=True,
        allow_delegation=False
    )

    return researcher, writer, reviewer


def run_team_demo(topic: str):
    """Run the multi-agent team demo"""

    tui = AgentTeamTUI()

    # Display UI
    tui.display_banner()
    tui.display_team_info()

    console.print(f"\n[bold cyan]📋 Mission:[/bold cyan] Research and write about '{topic}'\n")

    # Create agents
    researcher, writer, reviewer = create_research_team()

    # Define tasks
    tui.display_progress("Researcher", "Starting research phase...", "working")
    research_task = Task(
        description=f"""Conduct comprehensive research on {topic}.
        Focus on:
        - Key concepts and definitions
        - Current trends and developments
        - Important facts and statistics
        - Practical applications

        Provide a detailed research summary.""",
        expected_output="A comprehensive research report with key findings and insights",
        agent=researcher
    )

    tui.display_progress("Writer", "Preparing to draft content...", "working")
    writing_task = Task(
        description=f"""Using the research findings, write an engaging article about {topic}.
        The article should be:
        - Clear and accessible
        - Well-structured
        - Informative and engaging
        - 300-400 words

        Include an attention-grabbing introduction and a strong conclusion.""",
        expected_output="A well-written article ready for review",
        agent=writer
    )

    tui.display_progress("Reviewer", "Standing by for review...", "working")
    review_task = Task(
        description="""Review the written article for:
        - Accuracy and factual correctness
        - Clarity and readability
        - Grammar and style
        - Overall impact

        Provide the final polished version.""",
        expected_output="A polished, publication-ready article",
        agent=reviewer
    )

    # Create crew
    console.print("\n[bold yellow]🚀 Launching Team Collaboration...[/bold yellow]\n")

    crew = Crew(
        agents=[researcher, writer, reviewer],
        tasks=[research_task, writing_task, review_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    with console.status("[bold green]Agents collaborating...", spinner="dots"):
        result = crew.kickoff()

    # Display result
    tui.display_progress("Researcher", "Research complete", "done")
    tui.display_progress("Writer", "Article drafted", "done")
    tui.display_progress("Reviewer", "Review complete", "done")

    tui.display_result(str(result))


def main():
    """Main entry point"""

    console.print("\n[bold green]Welcome to the Multi-Agent Team Demo![/bold green]\n")

    # Get user input
    topic = Prompt.ask(
        "[cyan]What topic should the team research and write about?[/cyan]",
        default="Artificial Intelligence in Healthcare"
    )

    console.print()

    # Run demo
    try:
        run_team_demo(topic)
        console.print("\n[bold green]✅ Demo completed successfully![/bold green]\n")
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Demo interrupted by user.[/yellow]")
    except Exception as e:
        console.print(f"\n[bold red]Error: {e}[/bold red]")
        console.print("[dim]Make sure you have set your OPENAI_API_KEY environment variable.[/dim]")


if __name__ == "__main__":
    main()
