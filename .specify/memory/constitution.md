<!-- Sync Impact Report:
     Version change: 1.1.0 -> 2.0.0
     Modified principles: Tech Stack Requirements, Clean Architecture Implementation, Storage Strategy, Coding Standards Compliance, Testing Requirements, Workflow Governance
     Added sections: Backend Stack Requirements, Frontend Stack Requirements, Database Strategy, Authentication Strategy, Statelessness Principle
     Removed sections: UI Standards section (replaced with more comprehensive architecture guidance)
     Templates requiring updates: ✅ updated - plan-template.md, spec-template.md, tasks-template.md
     Follow-up TODOs: Need to verify all templates are updated to reflect new full-stack architecture requirements
-->
# Speckit Constitution

## Core Principles

### Tech Stack Requirements
All projects MUST use Python 3.13+ and the UV package manager for backend services, and TypeScript 5+ with Node.js 18+ for frontend applications. This ensures consistency across the development environment and leverages the latest language features and performance improvements. The choice of UV provides faster dependency resolution and installation compared to traditional tools. Projects MUST adopt a monorepo structure with `/backend` and `/frontend` directories.

### Clean Architecture Implementation
The system MUST follow Clean Architecture principles with strict separation between the Presentation Layer (Frontend) and the Logic Layer (Backend API). The backend must be stateless (REST API) while the frontend is the only way users interact with the data. This ensures testability, maintainability, and clear boundaries between concerns. The presentation layer should only handle user interface and interaction, while the logic layer contains all business rules and domain logic.

### Storage Strategy
All data storage MUST use PostgreSQL (Neon Serverless) with psycopg2-binary driver. This provides a robust, scalable, and reliable database solution that supports modern web applications. The database schema must be managed through SQLModel ORM to ensure consistency and maintainability.

### Coding Standards Compliance
All code MUST comply with PEP 8 standards for Python and TypeScript/JavaScript standards for frontend code. All functions must include type hinting, and all classes must have comprehensive docstrings. This ensures code quality, readability, and maintainability across the project. Type hints provide better IDE support and help catch errors early in the development process.

### Workflow Governance
All code must be developed following the full-stack development workflow with clear separation between frontend and backend tasks. Each task must define both frontend and backend requirements, with explicit acceptance criteria covering both layers. This ensures accountability, proper planning, and traceability throughout the development process.

### Testing Requirements
All backend logic MUST be testable via pytest and all frontend components MUST be testable via Jest or React Testing Library. Every business rule and function should be designed with testability in mind. Unit tests are mandatory for all business logic, integration tests should verify the interaction between frontend and backend, and end-to-end tests should cover user flows. Test-driven development is encouraged to ensure comprehensive coverage.

### Backend Stack Requirements
All backend services MUST be built with FastAPI, using SQLModel ORM for database operations and Uvicorn as the ASGI server. This ensures a modern, fast, and scalable backend architecture that integrates well with the frontend ecosystem. The backend must expose RESTful APIs that are documented with OpenAPI specifications.

### Frontend Stack Requirements
All frontend applications MUST be built with Next.js 15+ using the App Router, Tailwind CSS for styling, and Lucide React for icons. This provides a modern, performant, and developer-friendly frontend framework that integrates seamlessly with the backend. The frontend must be responsive and accessible across all device sizes.

### Database Strategy
All applications MUST use PostgreSQL (Neon Serverless) with psycopg2-binary driver. This provides a robust, scalable, and reliable database solution that supports modern web applications. Database schemas must be managed through SQLModel ORM to ensure consistency and maintainability. Migrations must be handled through Alembic or similar tools.

### Authentication Strategy
All applications MUST implement JWT-based authentication using Better Auth framework. This ensures secure, stateless authentication that integrates well with modern web applications. Sessions must be managed securely with proper token expiration and refresh mechanisms.

### Statelessness Principle
The Backend must be stateless (REST API). The Frontend must be the only way users interact with the data. This ensures scalability, reliability, and maintainability of the system. All session state must be managed on the frontend or through external services, not in the backend.

## Development Constraints

The project follows a full-stack development approach with specific requirements for both frontend and backend. All development must align with the current phase requirements and not implement features beyond the current scope. Focus on delivering working functionality across both frontend and backend layers.

## Workflow Requirements

The development process requires that each task be clearly defined with acceptance criteria covering both frontend and backend components before implementation begins. Code reviews are mandatory for all pull requests, and all tests must pass before merging. Continuous integration practices should be followed to ensure code quality and system stability.

## Governance

This constitution governs all development activities for the Speckit project. All team members must adhere to these principles, and any deviation requires explicit approval from the project guardian. Amendments to this constitution require documentation of the change, its impact, and approval from the core team.

**Version**: 2.0.0 | **Ratified**: 2025-12-28 | **Last Amended**: 2025-12-28