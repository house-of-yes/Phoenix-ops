## DYAD-PROTOCOL

### Overview
The dyad system provides a way for the AI runtime to recognize and act on **two-word semantic micro-commands** (“dyads”) within chat messages. Dyads are **interpreted live**, allowing dynamic and context-sensitive behavior.

### Dyad Recognition Rules
1. **Two words only** – a valid dyad must consist of exactly two words.
2. **Standalone or sentence-final** – dyads are recognized only when they appear as a standalone message or as the final sentence in a message.
3. **Misspellings tolerated** – minor spelling errors should be interpreted generously.
4. **Punctuation irrelevant** – all punctuation is stripped prior to recognition.
5. **Multilingual support** – synonyms in other languages map to the same dyad.

### Dyad Structure
- **Trigger words**: the two words that invoke the dyad.
- **Associated action**: the runtime function or protocol that executes when the dyad is recognized.
- **Optional metadata**: tags, priorities, or conditions that influence execution.

### Example Dyads
| Trigger | Action | Notes |
|---------|--------|-------|
| `load context` | load full Phoenix Ops context | reinstates all dyads and rules |
| `save state` | serialize current memory | stores MEMORY.state |
| `reset flow` | clear session buffers | resets transient context |

### Extensions
- Public dyads can be shared and extended.
- Private dyads remain in **extensions/private_overlays/**. 
- Dyads can include hooks for multilingual synonyms, dynamic evaluation, or context-sensitive conditions.

### Best Practices
- Keep triggers concise and semantically meaningful.
- Avoid overlapping triggers to prevent ambiguity.
- Maintain dyads in a **machine-readable YAML** (`core/DYADS.yaml`) for runtime consistency.

### Notes
- Dyads are **interpreted, not scripted**; the runtime determines the actual effect based on context.
- Adding new dyads is safe and does not require changes to the core engine.

