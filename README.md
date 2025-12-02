---

Phoenix Ops

Phoenix Ops is a deterministic context reconstruction and dyad recognition engine. It allows AI systems to instantly restore working context, recognize two-word semantic triggers ("dyads"), and extend functionality safely and modularly.


---

Features

Context Reconstruction: Restore context stacks deterministically from canonical snapshots.

Two-Word Dyads: Recognize standalone or final-sentence dyads.

Multilingual Support: Map synonyms across languages to the same dyad.

Punctuation and Typo Tolerance: Ignore punctuation and allow fuzzy matching.

Extension Hooks: Add private or experimental functionality safely.

Public & Private Separation: Core engine is public; sensitive/user-specific dyads live in extensions/private_overlays/.



---

Getting Started

Install

# Clone the repo
git clone https://github.com/YOUR_USERNAME/phoenix_ops.git
cd phoenix_ops

Example Usage

from core.context_loader import ContextLoader

# Callback function for dyad
def greet():
    print("Dyad triggered: Hello!")

# Canonical snapshot
canonical_data = {
    "context_stack": ["initial context entry"],
    "dyads": [
        {
            "canonical": "say hi",
            "callback": greet,
            "synonyms": ["dire bonjour"]
        }
    ],
    "extensions": []
}

loader = ContextLoader()
loader.load_canonical_context(canonical_data)

# Test inputs
loader.process_input("Say hi.")          # Triggered
loader.process_input("Dire bonjour!")    # Triggered
loader.process_input("Say hi there.")    # Ignored

print(loader.get_context())


---

Repo Structure

phoenix_ops/
├── core/                   # Core engine: context_loader, dyad_engine, utils
├── extensions/             # Private overlays and extension hooks
│   └── private_overlays/
├── public_docs/            # Documentation (DYAD-PROTOCOL.md)
├── examples/               # Example usage scripts
├── tests/                  # Unit tests
└── LICENSE


---

DYAD Protocol

See docs/DYAD-PROTOCOL.md for full details on:

Two-word recognition rules

Multilingual support

Punctuation and typo handling

Safe extension and redaction practices



---

License

MIT License — see LICENSE.









