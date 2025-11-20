# src/sqlguard/cli.py
from rich.console import Console
from rich.panel import Panel
from rich import box

from sqlguard.effects.animations import MatrixRain, CyberpunkSQLEditor, AnimatedAnalyzer
from sqlguard.core.analyzer import QueryAnalyzer
from sqlguard.formatters.console import ConsoleFormatter


def main():
    console = Console()

    # 1) Intro animation (fast, no ceremony)
    try:
        matrix = MatrixRain()
        matrix.run(duration=3)
    except Exception:
        # Fail silently if terminal doesn't support full animation
        pass

    # 2) Capture queries via editor
    editor = CyberpunkSQLEditor()
    queries_text = editor.get_queries()
    if not queries_text or not queries_text.strip():
        console.print("[bold yellow]No queries entered. Exiting.[/]")
        return

    # 3) Analyze
    analyzer = QueryAnalyzer(verbose=False)
    results_df = analyzer.analyze(queries_text, return_dataframe=True)

    # 4) Render vaporwave report
    formatter = ConsoleFormatter()
    formatter.format_analysis(results_df, title="SQLGuard Analysis")

    # 5) Optional animated “analysis complete” flourish
    try:
        aa = AnimatedAnalyzer()
        aa.glitch_transition(0.25)
    except Exception:
        pass


if __name__ == "__main__":
    main()
