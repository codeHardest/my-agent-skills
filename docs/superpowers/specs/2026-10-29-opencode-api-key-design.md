# OpenCode API Key Authentication Design

## Scope

Update `video-summarizer/scripts/generate_summary.py` so standalone summary generation authenticates with `OPENCODE_API_KEY` first and remains compatible with `ANTHROPIC_API_KEY`.

## Design

- Resolve the key in this order: `OPENCODE_API_KEY`, then `ANTHROPIC_API_KEY`.
- Pass the resolved value explicitly as `api_key` to `anthropic.Anthropic`.
- Resolve the endpoint in this order: `OPENCODE_BASE_URL`, then `ANTHROPIC_BASE_URL`, then the SDK default. Remove a terminal `/v1`, since the Anthropic SDK appends `/v1/messages` itself.
- Resolve `x-opencode-session` from `OPENCODE_SESSION_ID`, then `CLAUDE_CODE_SESSION_ID`, and otherwise generate one per script run. Preserve the model fallback chain, retries, and transcript fallback.
- If neither variable exists, raise a clear error naming both accepted variables without printing either value.

## Validation

- Verify `OPENCODE_API_KEY` wins when both variables exist.
- Verify `ANTHROPIC_API_KEY` remains a fallback.
- Verify `OPENCODE_BASE_URL` wins over `ANTHROPIC_BASE_URL` and that the latter remains a fallback.
- Verify missing credentials produce a clear error.
- Compile the Python script and confirm no key values appear in output.
