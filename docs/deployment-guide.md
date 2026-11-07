# Deployment Guide - Mekong Mobile Smart CRM (AI Track)

## 1. System Prerequisites & Environment
* **Operating System:** Linux (Ubuntu 22.04+), macOS, or Windows with WSL2.
* **Runtime & Tools:** 
  * Python 3.11+ or Docker Desktop (recommended for containerized deployment).
  * Git client.
* **Hardware Requirements:** Minimum 2GB RAM, 1GB free disk space.

## 2. Configuration & Environment Variables
Before running the application, configure the environment settings:
1. Copy the template environment file:
   ```bash
   cp .env.example .env 

   Verify that no production secrets or real API keys are hardcoded in the repository (ensuring public repo safety).

3. Build & Deployment Commands (≤ 2 Commands)
From an empty directory or cloned repository root, the system can be fully built and started using Docker Compose with at most 2 commands:
git clone [https://github.com/jasondoan08/cdtn1-DoanHoangQuan-l9.git](https://github.com/jasondoan08/cdtn1-DoanHoangQuan-l9.git)
cd cdtn1-DoanHoangQuan-l9
docker compose up --build -d
4. Verification: How to Check if the System Runs Correctly
To verify that the prediction service and API backend are running properly:

Check container health status:
docker compose ps
Test the prediction endpoint using curl or Postman:
curl -X POST "http://localhost:8080/du-doan" \
     -H "Content-Type: application/json" \
     -d '{"mo_ta": "Máy sạc không vào điện, cắm sạc không lên"}'
Expected Result: HTTP Status 200 OK with JSON response containing top_3 predictions and confidence scores.
5. Maintenance, Logs & Teardown
View application logs:
docker compose logs -f
Stop and clean up containers:
docker compose down
Security Checklist (7 Items)No.Security ItemStatusEvidence / Implementation Detail1No Secrets in Repo: No .env files or hardcoded API keys/passwords exist in the Git history.PASSEDVerified via manual inspection and Git history logs; uses .env.example.2Secure Passwords / Credentials: Database or user passwords are appropriately hashed or managed.PASSEDConfigured via environment variables; no raw plain-text credentials stored.3Input Validation: API endpoints strictly validate input types and lengths (preventing malformed payloads).PASSEDEnforced via Pydantic models (e.g., min_length=5), returning HTTP 422 on invalid data.4CORS Policy Configuration: Cross-Origin Resource Sharing is appropriately scoped.PASSEDConfigured in FastAPI app to restrict untrusted external origins.5Safe Error Handling: Error responses do not leak stack traces, table names, or connection strings.PASSEDCustom exception handlers catch errors and return clean JSON error codes.6Access Control (A01): Protected endpoints enforce proper user authentication/authorization checks.PASSEDVerified via test cases ensuring unauthorized access is blocked (HTTP 403/401).7Data Leakage Prevention: Training and testing data pipelines are strictly isolated.PASSEDScikit-learn Pipeline and StratifiedKFold implemented; verified via automated tests.