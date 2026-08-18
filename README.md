# Slack Export (`slack-export`)

**Category:** forensics · **Difficulty:** easy · **Points:** 200

A Slack/Discord export JSON still contains a message with the base64 blob.

## Run it

```bash
docker build -t sparflag/slack-export .
# `deca-ai start slack-export` (or the web UI) prints the docker run line with your
# SPARFLAG_SERVER + SPARFLAG_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is base64-encoded. Decode it to recover the flag.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
deca-ai submit slack-export 'sparflag{...}'
```

## Hints

- Search the export for long base64-looking strings.
- Decode the matching message.
