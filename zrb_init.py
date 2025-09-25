import os
import json
import requests
from zrb import CmdTask, cli, StrInput, make_task, AnyContext

code_review_task = cli.add_task(
    CmdTask(
        name="code-review",
        input=[
            StrInput("source", default="HEAD"),
            StrInput("target", default="main"),
        ],
        cmd="git diff {ctx.input.target} {ctx.input.source}"
    )
)


@make_task(
    name="submit-comment",
    input=StrInput("comment"),
    group=cli,
)
def submit_comment_task(ctx: AnyContext):
    comment = ctx.input.comment
    github_token = os.environ.get("GITHUB_TOKEN")
    github_event_path = os.environ.get("GITHUB_EVENT_PATH")
    github_repository = os.environ.get("GITHUB_REPOSITORY")

    if not all([github_token, github_event_path, github_repository]):
        ctx.log_error("Missing one or more required GitHub environment variables.")
        return

    with open(github_event_path, 'r') as f:
        event_data = json.load(f)

    pr_number = event_data.get("pull_request", {}).get("number")

    if not pr_number:
        ctx.log_error("Could not get PR number from the event payload.")
        return

    ctx.print(f"Commenting on PR #{pr_number}")

    payload = {"body": comment}
    api_url = f"https://api.github.com/repos/{github_repository}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        ctx.print("Comment posted successfully.")
    except requests.exceptions.RequestException as e:
        ctx.log_error(f"Failed to post comment: {e}")
        ctx.log_error(f"Response: {response.text}")
