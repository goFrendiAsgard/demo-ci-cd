from zrb import CmdTask, cli, StrInput

code_review_task = cli.add_task(
    CmdTask(
        name="code-review",
        input=[
            StrInput("source"),
            StrInput("target"),
        ],
        cmd="git diff {ctx.input.target} {ctx.input.source}"
    )
)