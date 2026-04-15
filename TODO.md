# TODO

## Done
- [x] Added a visual prediction result section in the web flow (`Prediction Result`).
- [x] Displayed the predicted iris class clearly in the UI.
- [x] Wired backend prediction output into template rendering for result display.
- [x] Kept form validation + error rendering stable in the same flow.
- [x] Updated/maintained `unittest` coverage for prediction payload behavior (`ok` / `prediction` / `errors`) and web result rendering.

## Next
- [ ] Add local static representative images per iris class (`setosa`, `versicolor`, `virginica`) and render the mapped image with the prediction.
- [ ] Add deterministic fallback behavior when a mapped class image file is missing.
- [ ] Extend `unittest` coverage for class-to-image mapping and fallback image behavior.
- [ ] Improve result-page styling (spacing, typography, image layout in `static/style.css`).
- [ ] Expand manual test scenarios for valid/invalid form input and image-missing cases.

## Later
- [ ] Finish API route parity (`POST /api/predict`) and align tests.
- [ ] Complete model-training path docs and local dev docs polish (`README.md`, `docs/dev-python.md`).
- [ ] Prepare deployment/readme polish while keeping Docker optional.
