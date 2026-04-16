# TODO

## Done
- [x] Flask app entrypoint with app factory (`create_app`) and web blueprint registration.
- [x] Browser flow implemented for `GET /` and `POST /predict`.
- [x] Input validation service for required numeric Iris fields.
- [x] Prediction service that returns deterministic class results for the web flow.
- [x] Predicted class image mapping for setosa / versicolor / virginica.
- [x] HTML templates and CSS for form entry, error rendering, and prediction result display.
- [x] Unit test coverage for web routes, validation service, prediction service, and model predictor utilities.

## In Progress
- [ ] API layer scaffolding exists (`routes/api.py`) but API routes are not implemented.
- [ ] Model training script placeholder exists (`model/train.py`) but training workflow is not implemented in code.

## Next Steps
- [ ] Implement `POST /api/predict` in `routes/api.py` using `services.prediction_service.predict_from_raw_input`.
- [ ] Register an API blueprint in `app.py` after API routes are implemented.
- [ ] Add `unittest` cases for API success and validation failure responses once API routes exist.
- [ ] Remove or wire `templates/result.html` so templates match actual rendered flow.

## Later / Nice to Have
- [ ] Add explicit numeric range validation (beyond required + numeric checks) for Iris inputs.
- [ ] Add unit tests for web fallback behavior when class image mapping is missing.
- [ ] Flesh out Dockerfile content for optional container run mode (without replacing WSL + Conda workflow).
