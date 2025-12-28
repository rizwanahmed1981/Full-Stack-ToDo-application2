<!-- Sync Impact Report:
     Version change: 1.0.0 -> 1.1.0
     Modified principles: Tech Stack Requirements
     Added sections: UI Standards section
     Removed sections: None
     Templates requiring updates: ⚠ pending - need to check plan-template.md, spec-template.md, tasks-template.md
     Follow-up TODOs: Need to verify all templates are updated to reflect new UI standards
-->

# Speckit Constitution

## Core Principles

### Tech Stack Requirements
All projects MUST use Python 3.13+ and the UV package manager. This ensures consistency across the development environment and leverages the latest language features and performance improvements. The choice of UV provides faster dependency resolution and installation compared to traditional tools. Projects MAY use the `rich` library for enhanced console UI capabilities, subject to approval by the project guardian.

### Clean Architecture Implementation
The system MUST follow Clean Architecture principles with strict separation between the Presentation Layer (CLI input/print) and the Logic Layer (Service/Models). This ensures testability, maintainability, and clear boundaries between concerns. The presentation layer should only handle user interaction and output formatting, while the logic layer contains all business rules and domain logic.

### Storage Strategy
All data storage MUST use in-memory lists for the current phase. No database systems should be implemented at this stage. This simplifies development and allows for rapid prototyping while keeping the focus on core functionality. Database integration will be considered in future phases when persistence becomes a requirement.

### Coding Standards Compliance
All code MUST comply with PEP 8 standards, include type hinting for all functions, and have docstrings for all classes. This ensures code quality, readability, and maintainability across the project. Type hints provide better IDE support and help catch errors early in the development process.

### Workflow Governance
No code may be written without a defined Task ID. Every piece of functionality must be traced back to an explicit task that defines its purpose, acceptance criteria, and requirements. This ensures accountability, proper planning, and traceability throughout the development process.

### Testing Requirements
All logic MUST be testable via pytest. Every business rule and function should be designed with testability in mind. Unit tests are mandatory for all business logic, and integration tests should verify the interaction between components. Test-driven development is encouraged to ensure comprehensive coverage.

### UI Standards
All console output MUST use `rich.console.Console` instead of standard `print()` statements to ensure consistent and enhanced user interface experiences. UI elements must follow these visual standards:
- Headers MUST be wrapped in `rich.panel.Panel` with style "bold magenta"
- Menus MUST be displayed with clear, colored numbering (e.g., `[1]`, `[2]`)
- Task lists MUST be rendered as `rich.table.Table` or formatted list with status icons (`[x]` or `[ ]`)
- Status indicators MUST use emoji or unicode characters for completion status (✅ or ○)

## Development Constraints

The project follows a hackathon-driven development approach with specific phases. All development must align with the current phase requirements and not implement features beyond the current scope. Focus on delivering working functionality over comprehensive documentation during the hackathon phase.

## Workflow Requirements

The development process requires that each task be clearly defined with acceptance criteria before implementation begins. Code reviews are mandatory for all pull requests, and all tests must pass before merging. Continuous integration practices should be followed to ensure code quality and system stability.

## Governance

This constitution governs all development activities for the Speckit project. All team members must adhere to these principles, and any deviation requires explicit approval from the project guardian. Amendments to this constitution require documentation of the change, its impact, and approval from the core team.

**Version**: 1.1.0 | **Ratified**: 2025-12-28 | **Last Amended**: 2025-12-28