# Demo CI/CD

This project demonstrates an automatic code review process using GitHub Actions.

## How It Works

This project uses a GitHub Action to automatically review pull requests. When a pull request is opened, the action will:

1.  **Fetch the changes:** The action checks out the code from the pull request.
2.  **Run a code review:** It uses `zrb` to perform a code review on the changes.
3.  **Post a comment:** The action posts the code review as a comment on the pull request.

## How to Use This Boilerplate

To use this CI/CD boilerplate in your own project, you'll need to configure the following:

### 1. Secrets

This boilerplate require the following secret to be setup under `Settings > Secrets and Variables > Actions`:

- ZRB_LLM_API_KEY: Your LLM API Key (i.e., for gemini, you can create API key through the following link: https://aistudio.google.com/api-keys)

### 2. Environment Variables

This boilerplate require the following variables to be setup under `Settings > Secrets and Variables > Actions`:

- ZRB_LLM_BASE_URL: Your openAI compatible API endpoint (e.g.,`https://generativelanguage.googleapis.com/v1beta/openai/`)
- ZRB_LLM_MODEL: Your preferred LLM Model (e.g., `gemini-2.5-flash`)

This boilerplate does not require any additional environment variables.

## Security

To prevent abuse, the workflow is configured to only run for pull requests created by repository members, owners, or collaborators. This is controlled by the following condition in the workflow file:

```yaml
if: github.event.pull_request.author_association == 'MEMBER' || github.event.pull_request.author_association == 'OWNER' || github.event.pull_request.author_association == 'COLLABORATOR'
```
