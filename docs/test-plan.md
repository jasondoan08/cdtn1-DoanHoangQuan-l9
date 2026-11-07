# Test Plan - Mekong Mobile Smart CRM (AI Track)

## 1. Scope & Exclusions
* **Testing Scope:**
  * FastAPIs for Churn Prediction (`/du-doan` endpoint).
  * Data pre-processing, text cleaning, and TF-IDF feature extraction pipelines.
  * Pydantic input payload validation (text string length, missing fields, correct JSON types).
  * Model inference logic, prediction confidence scores, and error handling structure.
* **Intentional Exclusions & Reasons:**
  * System administration UI & dashboard config: Excluded because it only handles static reading with no core business rules implemented yet.
  * Live database persistence & external authentication servers: Excluded as mock data and local service isolations are used for prototype scope.

## 2. Test Types & Quantity
* **Unit Tests (Service & Pipeline):** 4 test cases (testing text cleaning, vectorizer, and baseline classifier).
* **Integration & Boundary Tests:** 3 test cases (boundary input lengths, empty strings, multi-language/special characters).
* **API & Data Quality / Security Tests:** 3 test cases (verifying HTTP 200/422 status codes, A01 OWASP access controls, data leakage isolation between train/test folds).
* **Total:** 10 test cases executed.

## 3. Measurable Success Criteria
* 100% of executed test cases must achieve **PASS** status in automated `pytest` execution.
* Every implemented business rule (text prediction, input length check, error format) has at least 1 dedicated test case.
* **Zero Critical or Major bugs** remaining open in the active Bug Log.

## 4. Test Environment & Fixtures
* **Environment:** Python 3.11+ running inside lightweight local environment / Docker container.
* **Test Fixtures & Setup:** Mock JSON payloads and synthetic customer feedback samples located in `tests/test_fixtures.json`. Reset state before each test suite execution.