# System Overview

## Purpose 

This document describes the high-level architecture of the Reverse Engineering Platform.

The goal is to define the major subsystems of the application, their responsiblities, and the
boundaries between them before implementation begins.

The architecture is designed around the principle that deterministic analysis should produce
reliable information, while AI services should interpret and explain that information rather
than replace the underlying analysis process.

---

# Architectural Principles

## Separation of Responsibilities

The platform is divided into independent subsystems with clearly defined responsiblities.

The user interface should not understand binary analysis internals.

The analysis engine should not depend on presentation concerns.

AI services should consume analysis results rather than directly inspect raw executables.

---

## Deterministic Analysis First

Executable parsing, disassembly, metadata extraction, and graph construction should produce
consistent, testable results independent of AI components.

---

## Extensibility

The architecture should allow additional:

- executable formats
- analysis techniques 
- visualization methods
- AI providers

to be added without requiring major changes to unrelated components.

---

# High-Level Architecture

The platform consists of five primary subsystems:

1. Desktop Application
2. Analysis Engine
3. Storage Layer
4. AI Services
5. Shared Models


## Desktop Application

### Responsibility

The desktop application provides the user-facing environment for interacting with
analyzed software.

It is responsible for:

- Loading projects
- Displaying analysis results
- Providing navigation between functions and program components
- Visualizing relationships such as call graphs and control flow graphs
- Presenting AI-generated explanations

The desktop application should not perform binary analysis directly.

### Example Components

- Project Explorer
- Function Browser
- Assembly Viewer
- Graph Visualization
- AI Assistant Interface


## Analysis Engine

### Responsibility

The analysis engine performs the deterministic examination of executable files.

It is responsible for:

- Reading executable formats
- Extracting metadata
- Identifying program structures
- Performing disassembly
- Building relationships between program components

The analysis engine is the source of truth for information about analyzed binaries.

### Example Components

- Executable Parser
- Disassembler
- Function Analyzer
- Control Flow Graph Builder
- Metadata Extractor


## Storage Layer

### Responsibility 

The storage layer persists information required by the platform.

It is responsible for:

- Saving projects
- Storing analysis results
- Managing user annotations
- Persisting search indexes and embeddings

The storage layer should allow analysis results to be reused without repeating expensive
analysis operations.

### Example Data

- Projects
- Executable Metadata
- Functions
- Instructions
- Graph Structures
- AI Conversations
- User Notes


## AI Services

### Responsibility

The AI subsystem provides intelligent assistance by interpreting existing analysis results.

It is responsible for:

- Generating function explanations
- Answering questions about analyzed software
- Performing semantic search
- Creating summaries of program behavior

The AI subsystem does not determine facts about the executable.

Instead, it receives verified analysis information and produces human-readable interpretations.


## Shared Models

### Responsibility

Shared models define the data structures exchanged between subsystems.

They provide a common vocabulary for representing concepts within the system.

Examples:

- Executable
- Function
- Instruction
- Basic Block
- Control Flow Graph
- Analysis Result


# Component Communication

The platform is designed around a modular architecture where major components communicate through
clearly defined boundaries.

The initial implementation will consist of two primary applications: 

- Desktop Application
- Analysis Engine

Both components will run locally and communicate through a defined interface.

This approach provides separation of responsibilities without introducing unnecessary 
distributed-system complexity.

---

## Desktop Application vs Analysis Engine

The Desktop Application is responsible for:

- User interaction
- Project management
- Visualization 
- Displaying analysis results

The Analysis Engine is responsible for:

- Executable parsing
- Static analysis
- Disassembly
- Metadata extraction
- Generating structured analysis results

The Desktop Application should never need to understand how analysis is performed.

The Analysis Engine should never need to understand how results are presented.

Communication between these components should occur through structured messages and 
shared data contracts.

---

## Future Expansion

This architecture allows future capabilities without requiring major redesign:

- Remote analysis execution
- Additional analysis engines
- Plugin systems
- Alternative user interfaces
- Local or remote AI providers


### First Version Flow Concept

User

 ↓

Desktop Application

 ↓

Analysis Engine

 ↓

Executable File


Analysis Results

 ↓

Storage Layer

 ↓

AI Services

 ↓

Explanation Presented to User