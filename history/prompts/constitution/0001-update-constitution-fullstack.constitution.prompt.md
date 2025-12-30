---
id: 0001
title: update-constitution-fullstack
stage: constitution
date: 2025-12-28
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 001-console-task-app
user: ecomw
command: sp.constitution
labels: ["fullstack", "webapp", "architecture", "constitution", "update"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - null
---

## Prompt

You are @speckit-plus.

We are starting **Phase II: Full-Stack Web App**. Update `specs/speckit.constitution` with these major changes:

1.  **Project Structure:** Monorepo. `/backend` (Python/FastAPI) and `/frontend` (TypeScript/Next.js).
2.  **Backend Stack:** FastAPI, SQLModel (ORM), Uvicorn.
3.  **Frontend Stack:** Next.js 15+ (App Router), Tailwind CSS, Lucide React (Icons).
4.  **Database:** PostgreSQL (Neon Serverless). Use `psycopg2-binary` driver.
5.  **Auth:** Better Auth (JWT) implementation.
6.  **Principle:** The Backend must be stateless (REST API). The Frontend must be the only way users interact with the data.

Goal: Rewrite the constitution to govern a distributed full-stack system.

## Response snapshot

Updated the Speckit Constitution to transition from a console-based application to a full-stack web application with the following major changes:

1. **Project Structure**: Changed from single project to monorepo with `/backend` and `/frontend` directories
2. **Backend Stack**: Specified FastAPI, SQLModel ORM, and Uvicorn as required technologies
3. **Frontend Stack**: Specified Next.js 15+, Tailwind CSS, and Lucide React as required technologies
4. **Database Strategy**: Transitioned from in-memory storage to PostgreSQL (Neon Serverless) with psycopg2-binary driver
5. **Authentication**: Specified JWT-based authentication using Better Auth framework
6. **Statelessness Principle**: Established that backend must be stateless (REST API) and frontend is the only user interface

The updated constitution now governs a distributed full-stack system with clear separation between frontend and backend responsibilities.

## Outcome

- ✅ Impact: Major architectural shift from console app to full-stack web application
- 🧪 Tests: No tests affected - this is a governance document update
- 📁 Files: Updated .specify/memory/constitution.md
- 🔁 Next prompts: /sp.plan, /sp.spec, /sp.plan for new full-stack project
- 🧠 Reflection: Constitution successfully updated to support modern web application architecture

## Evaluation notes (flywheel)

- Failure modes observed: None - constitution update completed successfully
- Graders run and results (PASS/FAIL): N/A for governance document
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Implement /sp.plan for new full-stack feature
