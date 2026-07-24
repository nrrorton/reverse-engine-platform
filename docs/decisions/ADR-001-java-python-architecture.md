# ADR-001: Separate Java Desktop Application and Python Analysis Engine

## Status

Accepted

## Date

2026-07-24

## Context

The Reverse Engineering Platform requires both a rich user interface and access to mature
binary analysis and AI ecosystems.

Java and Python provide complementary strengths:

- Java provides strong object-oriented design capabilities, mature desktop application support,
and a large ecosystem for building complex applications.
- Python provides extensive support for reverse engineering, machine learning, and AI-related tooling.

A single-languer approach would either limit access to important libraries or reduce opportunities
to learn different engineering concepts. (Ultimately, this is a learning opportunity first and foremost)

## Decision

The platform will be developed as two primary components:

1. A Java-based desktop application.
2. A Python-based analysis engine.

The components will communicate through a clearly defined interface.

Initially, both components will operate locally on the user's machine.

## Alternative Considered

### Python-only Application

Advantages:

- Strongest reverse engineering and AI ecosystem.
- Faster initial development.

Disadvantages:

- Less opportunity to deepen Java and object-oriented design skills.
- Desktop application architecture would be less aligned with learning goals.

---

### Java-only Application

Advantages:

- Single language ecosystem.
- Strong object-oriented design practice.

Disadvantages:

- Reduced access to mature reverse engineering and AI libraries.
- More effort required to implement or integrate analysis capabilities.

---

### Fully Distributed Architecture

Advantages:

- Maximum scalability.
- Natural separation of services.

Disadvantages:

- Introduces unnecessary complexity.
- Adds deployment and operational concerns before they provide value.

## Consequences

Positive:

- Each component uses the language best suited for its responsibilities.
- Clear separation of concerns.
- Easier future expansion.

Negative:

- Requires defining communication contracts.
- Requires maintaining two codebases.
- Debugging across language boundaries may require additional tooling.

## Review Criteria

This decision should be revisited if:

- Communication complexity becomes a significant burden.
- A different architecture provides clear advantages.
- The project requirements expand substantially.