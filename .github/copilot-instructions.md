# Copilot Instructions for AI Coding Agents

## Project Overview
This repository contains Python training materials, organized by topic and date. It is structured for educational purposes, with each folder representing a lesson or concept. There is no monolithic application; instead, the codebase is a collection of scripts and examples.

## Directory Structure & Key Patterns
- `01_python_basics/`, `02_variables/`, `03_ctrl_stmts/`, `04_strings/`, `05_Dictionaries/`, `Tuples/`, `codes.py/`: Each folder contains scripts for a specific Python topic or lesson. File names often reflect the lesson date or concept.
- Scripts are generally independent and not meant to be run as a single application.
- Example: `05_Dictionaries/dict.py` demonstrates dictionary usage; `01_python_basics/lists.py` covers lists.

## Developer Workflows
- There is no build system or test harness. Run scripts directly using Python:
  ```powershell
  python <path-to-script>
  ```
- No external dependencies are required; all code uses the Python standard library.
- No package management (e.g., requirements.txt) is present.

## Project Conventions
- File and folder names may use dates (e.g., `18 August`) or topics (e.g., `lists.py`).
- Scripts are self-contained and may include demonstration code, exercises, or notes.
- No formal module structure or imports between lesson scripts.
- Comments and docstrings are minimal; code is intended for instructional clarity.

## Guidance for AI Agents
- When adding new examples, follow the existing pattern: create a new script in the relevant topic folder.
- Do not introduce external dependencies unless explicitly requested.
- Keep code simple and focused on illustrating the concept.
- If updating or refactoring, preserve the educational intent and clarity of examples.
- Reference the README for the high-level project purpose.

## Example
To add a new lesson on sets:
- Create `06_sets/sets.py` and place example code there.

---
For questions about project structure or conventions, review the folder organization and existing scripts for guidance.
