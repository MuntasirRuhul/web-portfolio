# Working rules for this repo

## Session hand-off (the user's standing rule)

When this session's context gets to about **500k tokens** (or replies start getting slow or expensive), don't keep going in the same session. Hand off:

1. Commit and push all work to `atelier-site`.
2. Update the **START HERE** section of `HANDOFF-NEXT.md`: what's done, what's next, open questions, any new user preferences.
3. Open a new Claude Code session on `MuntasirRuhul/web-portfolio`, branch `atelier-site` (outcome branch `atelier-site`), with the prompt: "Read HANDOFF-NEXT.md (START HERE first). Reply in a few lines: what's done, what's next, and ask which page to build. Don't start building until I answer. Keep replies short."
4. Tell the user the new session's name, and that the old one can be kept or archived (archive only if they say so).

Do this every time; don't wait to be asked.

## Other standing preferences

- Keep replies short; the user watches token use.
- Desktop first (1440px). Phone and tablet come in a later pass.
- Every page must pass `node tools/audit.mjs --desktop <page>` before publishing.
- Pages must feel specific to Elena's studio, never generic.
