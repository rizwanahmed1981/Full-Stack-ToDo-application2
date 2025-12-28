# Tasks: Console Task App

**Input**: Design documents from `/specs/001-console-task-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 [P] Create project structure per implementation plan
- [X] T002 [P] Initialize Python project with UV dependencies
- [X] T003 [P] Create README.md with project overview and usage instructions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T004 [P] Create src/ directory structure
- [X] T005 [P] Create tests/ directory structure
- [X] T006 [P] Create pyproject.toml with project metadata and dependencies
- [X] T007 [P] Create src/__init__.py for package initialization
- [X] T008 [P] Create tests/__init__.py for test package initialization

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to create new tasks with title and optional description

**Independent Test**: Can be fully tested by entering a title and optional description, and verifying that a new task with a unique ID is created and displayed in the system.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T009 [P] [US1] Unit test for Task model validation in tests/unit/test_models.py
- [X] T010 [P] [US1] Unit test for TodoService.add_task in tests/unit/test_service.py

### Implementation for User Story 1

- [X] T011 [P] [US1] Create Task model in src/models.py
- [X] T012 [P] [US1] Create TodoService class in src/service.py
- [X] T013 [US1] Implement add_task method in src/service.py
- [X] T014 [US1] Implement get_all_tasks method in src/service.py
- [X] T015 [US1] Implement get_task_by_id method in src/service.py
- [X] T016 [US1] Implement validation logic for task title in src/service.py
- [X] T017 [US1] Create main CLI interface in src/main.py
- [X] T018 [US1] Implement main menu loop in src/main.py
- [X] T019 [US1] Implement add task functionality in src/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 10: Refactoring - ID Generation (Priority: P1)

**Goal**: Refactor ID generation to use user-friendly `tidXX` format instead of UUIDs

**Independent Test**: Can be fully tested by verifying that new tasks get IDs in `tidXX` format

### Implementation for Refactoring

- [X] T007 [US1] Refactor ID Generation in src/service.py to use `tid` + padded number format
- [X] T008 [US1] Update Unit Tests to verify new ID format in tests/unit/test_service.py
- [X] T009 [US1] Verify UI displays new IDs correctly in src/main.py

**Checkpoint**: At this point, all tasks should use the new ID format consistently

---

## Phase 4: User Story 2 - View List (Priority: P1)

**Goal**: Allow users to see all tasks with their ID, Title, Status, and Description

**Independent Test**: Can be fully tested by viewing the list of tasks and verifying that all existing tasks are displayed with their ID, Title, Status, and Description.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T020 [P] [US2] Unit test for TodoService.get_all_tasks in tests/unit/test_service.py

### Implementation for User Story 2

- [ ] T021 [US2] Implement view list functionality in src/main.py
- [ ] T022 [US2] Implement display formatting for tasks in src/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Complete (Priority: P2)

**Goal**: Allow users to toggle the status of a specific task from incomplete to complete or vice versa

**Independent Test**: Can be fully tested by selecting a task and toggling its status, then verifying the status change is reflected in the system.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T023 [P] [US3] Unit test for TodoService.toggle_task_status in tests/unit/test_service.py

### Implementation for User Story 3

- [ ] T024 [US3] Implement toggle_task_status method in src/service.py
- [ ] T025 [US3] Implement mark complete functionality in src/main.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task (Priority: P3)

**Goal**: Allow users to modify the details of an existing task by selecting it by ID

**Independent Test**: Can be fully tested by selecting a task by ID and modifying its details, then verifying the changes are saved.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T026 [P] [US4] Unit test for TodoService.update_task in tests/unit/test_service.py

### Implementation for User Story 4

- [ ] T027 [US4] Implement update_task method in src/service.py
- [ ] T028 [US4] Implement update task functionality in src/main.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Task (Priority: P3)

**Goal**: Allow users to remove a task by selecting it by ID

**Independent Test**: Can be fully tested by selecting a task by ID and deleting it, then verifying it no longer appears in the task list.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T029 [P] [US5] Unit test for TodoService.delete_task in tests/unit/test_service.py

### Implementation for User Story 5

- [ ] T030 [US5] Implement delete_task method in src/service.py
- [ ] T031 [US5] Implement delete task functionality in src/main.py

**Checkpoint**: At this point, User Stories 1, 2, 3, 4 AND 5 should all work independently

---

## Phase 8: User Story 6 - Exit Application (Priority: P1)

**Goal**: Provide a proper way to end the session cleanly

**Independent Test**: Can be fully tested by selecting the exit option and verifying the application terminates cleanly.

### Tests for User Story 6 (OPTIONAL - only if tests requested) ⚠️

- [X] T032 [P] [US6] Unit test for exit functionality in tests/unit/test_cli.py

### Implementation for User Story 6

- [ ] T033 [US6] Implement exit functionality in src/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 11: UI Overhaul - Rich Integration

### Goal
Implement Rich-based UI components to replace current print-based interface.

### Independent Test Criteria
- New UI functions render properly with Rich formatting
- All existing functionality remains intact
- Visual indicators match requirements (icons ✅ and ○)

### Tasks

- [ ] T010 [P] Update pyproject.toml to include rich dependency and run uv sync
- [ ] T011 [P] Verify Rich installation by importing in main.py
- [ ] T012 [P] [US2] Create render_header() function in main.py using Rich Panel
- [ ] T013 [P] [US2] Create render_menu() function in main.py using Rich color markup
- [ ] T014 [P] [US2] Refactor display_tasks() to use Rich Table with Status, ID, Title/Description columns
- [ ] T015 [P] [US2] Replace get_user_input() with Rich Prompt.ask for better input handling
- [ ] T016 [P] [US2] Update main.py to initialize global Console instance
- [ ] T017 [US2] Integrate new Rich UI functions into main application loop
- [ ] T018 [US2] Test all menu options work with new Rich UI implementation
- [ ] T019 [P] Update error handling to use Rich styled messages
- [ ] T020 [P] Update README.md to reflect Rich UI features
- [ ] T021 [P] Test application with various input scenarios
- [ ] T022 [P] Verify error handling messages display properly with Rich
- [ ] T023 [P] Performance test to ensure Rich doesn't significantly impact response times

**Checkpoint**: At this point, the application should have a fully enhanced UI with Rich components

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T034 [P] Add comprehensive error handling and user-friendly messages
- [ ] T035 [P] Add input validation for all user interactions
- [ ] T036 [P] Add visual indicators for task status ([x] vs [ ])
- [ ] T037 [P] Update README.md with complete usage instructions
- [ ] T038 [P] Run integration tests for CLI interactions in tests/integration/test_cli.py
- [ ] T039 [P] Run all unit tests to ensure full functionality
- [ ] T040 [P] Validate quickstart.md instructions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable
- **User Story 6 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4/US5 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for Task model validation in tests/unit/test_models.py"
Task: "Unit test for TodoService.add_task in tests/unit/test_service.py"

# Launch all models for User Story 1 together:
Task: "Create Task model in src/models.py"
Task: "Create TodoService class in src/service.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Add User Story 6 → Test independently → Deploy/Demo
8. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
   - Developer F: User Story 6
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence