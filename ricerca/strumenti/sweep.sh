S=$(cd "$(dirname "$0")" && pwd)
RX='is there (a|an|any) (tool|app|software|program|service|plugin|extension|way to automate)|does anyone (know|use) (a|of|any) (tool|app|software)|I wish there (was|were)|would (happily |gladly )?pay for|wrote a (python |small |simple )?script|built a (python |small |simple )?script|(doing|do) (this|it|them) manually|manually (copy|enter|type|update|check|track)|copy(ing)? and past|looking for (a |an )?(software|tool|app)|too expensive|overkill for|why (doesn.t|does no) .{0,40} (support|have|let)'
for sub in "$@"; do
  python3 $S/reddit_scansione.py $sub "$RX" 2025-01-01 2026-10-05 ${PAGES:-15} > $S/../dati/reddit_$sub.txt 2>&1
  sleep 3
done
