# Full-Stack Task Management Application

This is a full-stack task management application built with FastAPI (backend) and Next.js (frontend).

## Project Structure

```
.
├── backend/                 # FastAPI backend
│   ├── app/                 # Application code
│   │   ├── api/             # API routes
│   │   ├── models.py        # Database models
│   │   ├── db.py            # Database configuration
│   │   └── main.py          # FastAPI application
│   └── pyproject.toml       # Python dependencies
├── frontend/                # Next.js frontend
│   ├── src/
│   │   ├── app/             # Next.js pages
│   │   ├── components/      # React components
│   │   ├── lib/             # API clients
│   │   └── types/           # TypeScript types
│   └── package.json         # JavaScript dependencies
└── specs/                   # Documentation and specifications
```

## Backend Setup (FastAPI)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install --break-system-packages -e .
   ```

3. Run the backend server:
   ```bash
   uv run fastapi dev app/main.py
   ```

   The backend will be available at http://localhost:8000

## Frontend Setup (Next.js)

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the frontend development server:
   ```bash
   npm run dev
   ```

   The frontend will be available at http://localhost:3000

## API Endpoints

- `GET /api/tasks` - List all tasks
- `POST /api/tasks` - Create a new task
- `PUT /api/tasks/{id}` - Update a task
- `DELETE /api/tasks/{id}` - Delete a task
- `PATCH /api/tasks/{id}/complete` - Toggle task completion status

## Features Implemented

1. **Core Task Management** (User Story 1 - P1):
   - Create, read, update, and delete tasks
   - Task completion toggling
   - Responsive UI with Tailwind CSS

2. **Backend Architecture**:
   - FastAPI with SQLModel ORM
   - PostgreSQL database (with SQLite fallback)
   - CORS middleware for frontend-backend communication
   - Proper API validation and error handling

3. **Frontend Architecture**:
   - Next.js 15+ with App Router
   - TypeScript type safety
   - React components with proper state management
   - Tailwind CSS for responsive design