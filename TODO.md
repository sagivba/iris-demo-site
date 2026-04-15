# TODO

## מטרה

להשלים אפליקציית דוגמה קטנה אך מלאה ב־Flask לחיזוי Iris, עם שכבות ברורות (routes / services / model), תיעוד עדכני, והרצה מקומית יציבה.

## כללים גלובליים

- להשתמש ב־Flask בלבד.
- לפתח לפי WSL + Conda + VS Code.
- להשתמש ב־`unittest` בלבד (ללא `pytest`).
- לשמור שינויים קטנים וממוקדים.
- לא לבצע ריפקטור רחב ללא בקשה מפורשת.
- לא להוסיף מסד נתונים.
- לא לאמן מודל בזמן request.
- לשמור על route handlers דקים וללא לוגיקת ML.
- לעדכן תיעוד כשפקודות/התנהגות/מבנה משתנים.

## סדר תלות

Task 01 → Task 02 → Task 03 → Task 04 → Task 05 → Task 06 → Task 07 → Task 08 → Task 09 → Task 10 → Task 11 → Task 12 → Task 13 → Task 14

---

## Task 01 - השלמת קבצי Bootstrap ראשוניים
- [ ] להבטיח שכל קבצי הבסיס קיימים ומכילים תוכן מינימלי תקין (`.env`, קבצי `.vscode`, `ci.yml` ועוד).
- [ ] להשלים placeholders חסרים כך שהשלד כולו עקבי (כולל קבצים שכרגע ריקים לגמרי).

## Task 02 - אפליקציית Flask מינימלית עם דף בית
- [x] אפליקציה ניתנת להרצה עם `app.py` ו־`create_app`.
- [x] הנתיב `/` מחזיר 200 ומציג טופס Iris בסיסי.

## Task 03 - תצורת VS Code ו־Workflow מקומי
- [ ] להשלים `.vscode/settings.json`, `.vscode/launch.json`, `.vscode/tasks.json`.
- [ ] להשלים `docs/dev-python.md` עם זרימת עבודה מלאה ל־WSL + Conda + unittest.
- [ ] להוסיף/לתעד `PYTHONPATH` וקונפיגורציית הרצה/בדיקות.

## Task 04 - שכבת מודל: אימון ושמירת ארטיפקט
- [ ] לממש `model/train.py` (טעינת Iris, אימון, שמירת מודל לדיסק).
- [ ] לתעד פקודת אימון בפועל ב־README ובתיעוד המפתחים.

## Task 05 - טעינת מודל ושירות חיזוי
- [ ] לחבר את `services/prediction_service.py` ל־`model/predictor.py` במקום חיזוי placeholder.
- [ ] להבטיח שהשירות מחזיר `predicted_class_index` ו־`predicted_class_label` על סמך מודל אמיתי.

## Task 06 - שכבת ולידציה לקלט
- [x] קיימת ולידציה מפורשת לכל 4 השדות (`required` + המרה למספר).
- [x] הוולידציה מופרדת לשירות וניתנת לשימוש חוזר.

## Task 07 - זרימת UI מלאה (טופס + תוצאה)
- [x] טופס HTML כולל את 4 שדות Iris.
- [x] שליחה תקינה מציגה דף תוצאה עם חיזוי וקלטים.
- [x] שליחה לא תקינה מציגה שגיאות ברורות למשתמש.
- [ ] לשפר סגנון בסיסי ב־`static/style.css` (כרגע ריק).

## Task 08 - נתיב API ל־JSON
- [ ] לממש `POST /api/predict` ב־`routes/api.py`.
- [ ] להחזיר תגובת JSON תקינה גם בהצלחה וגם בשגיאת ולידציה.

## Task 09 - בדיקות אפליקציה (Web + API)
- [ ] להשלים `tests/test_api.py`.
- [x] קיימות בדיקות Web בסיסיות (`tests/test_app.py`).
- [ ] לוודא כיסוי גם למסלולי API תקינים ושגויים.

## Task 10 - בדיקות שכבת שירותים
- [ ] ליישר `tests/test_services.py` לממשק הקיים ב־`services/prediction_service.py`.
- [ ] להבטיח שהבדיקות דטרמיניסטיות ועוברות ב־`python -m unittest discover -v`.

## Task 11 - README מלא ומעודכן
- [ ] לעדכן README כך שישקף מצב מימוש אמיתי (לא "scaffold בלבד" אם בפועל יש Web flow פעיל).
- [ ] להוסיף הנחיות מדויקות להרצה, בדיקות, שימוש API, וארכיטקטורה נוכחית.

## Task 12 - תיעוד מפתחים
- [ ] להשלים `docs/dev-python.md` (כרגע ריק).
- [ ] לתעד הרצה, בדיקות, אימון מחדש, ניפוי תקלות, ו־VS Code workflow.

## Task 13 - CI
- [ ] לממש `.github/workflows/ci.yml` עם הרצת unit tests על `push` ו־`pull_request`.

## Task 14 - Docker אופציונלי
- [ ] לממש `Dockerfile` בסיסי להרצה אופציונלית.
- [ ] לעדכן README כדי להבהיר ש־Docker אופציונלי בלבד ולא הזרימה הראשית.

---

## בדיקות מצב לפי אזורים (Checklist מהיר)

### מבנה פרויקט
- [x] קיימים נתיבים עיקריים: `routes/`, `services/`, `model/`, `templates/`, `static/`, `tests/`.
- [ ] קבצי היגיינת ריפו מרכזיים עדיין חסרים/ריקים בחלקם (`.env`, `.vscode/*`, `ci.yml`).

### Model layer
- [x] יש `model/predictor.py` עם טעינת מודל ו־predict.
- [ ] `model/train.py` עדיין לא ממומש.

### Validation
- [x] קיימת ולידציה מפורשת לארבעת השדות.

### Services
- [ ] שירות החיזוי עדיין placeholder ולא מחובר בפועל למודל המאומן.

### Routes
- [x] קיימים Web routes (`/`, `/predict`) עם זרימה תקינה.
- [ ] API route עדיין לא קיים.

### UI / Templates / Static
- [x] קיימים `base/index/result` עם זרימת טופס ותוצאה.
- [ ] `static/style.css` ריק.

### Tests
- [ ] `unittest` discovery כרגע לא יציב עקב חוסר התאמה בין tests לשירותים ו־API חסר.

### README + Docs
- [ ] README לא מסונכרן במלואו עם המצב בפועל.
- [ ] `docs/dev-python.md` ריק.

### מוכנות להרצה מקומית
- [x] אפליקציית Web בסיסית עולה.
- [ ] אימון מודל, API, ותיעוד סביבת פיתוח עדיין לא מוכנים מקצה לקצה.
