#!/usr/bin/env bash
# Source-consistency lint for the rutter plugin.
# Deliberately NOT the test seam: it reads source text, not behaviour.
# Catches the drift classes that a plugin load cannot see.
set -uo pipefail
cd "$(dirname "$0")/.."
fail=0
report() { printf '  %s\n' "$2"; printf '%s\n' "$3" | sed 's/^/      /'; fail=1; }

# 1. One ticket vocabulary. plan:* was the pre-1.0 set; meridian:* is canonical.
hits=$(grep -rnE '\bplan:(map|judgment|research|experiment|task|route)\b' skills/ agents/ references/ 2>/dev/null || true)
[ -n "$hits" ] && report 1 "foreign ticket vocabulary (plan:*) — canonical set is meridian:*" "$hits"

# 2. One mode vocabulary.
hits=$(grep -rnE '\bready-for-(agent|human)\b' skills/ agents/ references/ 2>/dev/null || true)
[ -n "$hits" ] && report 2 "foreign mode vocabulary (ready-for-*) — canonical set is mode:agent / mode:human" "$hits"

# 3. No hardcoded package manager in shipped skills or agents.
hits=$(grep -rnE '(pnpm|yarn|bun) [a-z:]+|npm run [a-z:]+' skills/ agents/ --include='*.md' 2>/dev/null || true)
[ -n "$hits" ] && report 3 "hardcoded build command — resolve via references/commands.md instead" "$hits"

# 4. Agent references must be namespaced; bare names resolve to a different agent.
hits=$(grep -rnE '`(scout|builder|reviewer|auditor|sweeper|drill)`' skills/ agents/ 2>/dev/null || true)
[ -n "$hits" ] && report 4 "bare agent reference — plugin agents only resolve as rutter:<agent>" "$hits"

# 5. No origin-project residue.
hits=$(grep -rniE '\borakl\b' skills/ agents/ references/ evals/ 2>/dev/null || true)
[ -n "$hits" ] && report 5 "origin-project reference leaked into shipped content" "$hits"

# 6. Cross-skill pointers inside the plugin must use ${CLAUDE_PLUGIN_ROOT}.
hits=$(grep -rnE '\.claude/skills/(meridian|transit|convoy)\b' skills/ agents/ 2>/dev/null || true)
[ -n "$hits" ] && report 6 "sibling skill referenced by project path — use \${CLAUDE_PLUGIN_ROOT}" "$hits"

if [ "$fail" -eq 0 ]; then echo "rutter lint: clean"; else echo; echo "rutter lint: FAILED"; fi
exit "$fail"
