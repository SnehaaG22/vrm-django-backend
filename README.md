# VRM / TPRM Backend (Django)

Vendor Risk Management (VRM) system built with Django & DRF to manage vendor onboarding, assessments, evidence, reviews, remediations, renewals, and audit logs.

---

## Tech Stack

- Backend: Python 3.11, Django, Django REST Framework
- Auth: JWT (SimpleJWT) + RBAC
- DB: PostgreSQL
- Async: Celery + Redis
- Storage: MinIO (S3 compatible)
- API Docs: drf-spectacular (Swagger)
- DevOps: Docker Compose

---

---

## Setup (Local – Docker)

### 1. Prerequisites
- Docker Desktop (running)
- Python 3.11 (optional for local dev)

### 2. Environment file
Create `.env` inside `vrm/` folder (do NOT commit):


### 3. Start services
```bash
docker compose up -d



