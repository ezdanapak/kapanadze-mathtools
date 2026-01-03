# PyPI Trusted Publishing - სწრაფი საცნობარო

## 🔐 PyPI-ზე შესასვლელი მონაცემები

როცა PyPI-ზე შედიხარ და ქმნი "Trusted Publisher"-ს, შეავსე ეს ველები:

```
┌─────────────────────────────────────────────────────────┐
│ Add a new pending publisher                             │
├─────────────────────────────────────────────────────────┤
│                                                           │
│ PyPI Project Name: kapanadze-mathtools                   │
│ (ეს არის შენი პროექტის სახელი PyPI-ზე)                   │
│                                                           │
│ Owner: შენი_github_username                              │
│ (შენი GitHub username, მაგ: kapogeo)                      │
│                                                           │
│ Repository name: kapanadze-mathtools                     │
│ (GitHub repository-ს სახელი)                              │
│                                                           │
│ Workflow name: publish.yml                               │
│ (GitHub Actions workflow ფაილის სახელი)                   │
│                                                           │
│ Environment name: pypi                                   │
│ (GitHub Environment - optional, მაგრამ რეკომენდებული)     │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

## 📝 მაგალითი კონკრეტული მონაცემებით

თუ შენი GitHub username არის `kapogeo`:

```
PyPI Project Name:     kapanadze-mathtools
Owner:                 kapogeo
Repository name:       kapanadze-mathtools
Workflow name:         publish.yml
Environment name:      pypi
```

## ⚠️ მნიშვნელოვანი დეტალები

1. **PyPI Project Name** უნდა იყოს უნიკალური მთელ PyPI-ზე
   - თუ `kapanadze-mathtools` უკვე დაკავებულია, სცადე:
   - `kapanadze-mathtools-geo`
   - `kapogeo-mathtools`
   - `mathtools-kapanadze`

2. **Owner** - ეს არის შენი GitHub username (არა email!)
   - შეამოწმე: https://github.com/შენი_username

3. **Workflow name** - ზუსტად ისე როგორც ფაილი შექმენი:
   - ✅ `publish.yml`
   - ❌ `.github/workflows/publish.yml` (მთელი path არ უნდა!)
   - ❌ `publish.yaml` (გაფრთხილდი extension-ზე!)

4. **Environment name** - შექმენი GitHub-ზე Repository Settings → Environments
   - სახელი: `pypi`
   - ეს იძლევა დამატებით უსაფრთხოებას

## 🚀 შემდეგი ნაბიჯები ფორმის შევსების შემდეგ

1. ✅ დააჭირე "Add" ღილაკს PyPI-ზე
2. ✅ შექმენი GitHub Release (tag: v0.1.0)
3. ✅ GitHub Actions ავტომატურად გააკეთებს დანარჩენს
4. ✅ 2-3 წუთში შენი package იქნება PyPI-ზე!

## 🔍 როგორ შევამოწმო, რომ გამოვიდა?

```bash
# 1. ახალ terminal-ში
pip install kapanadze-mathtools

# 2. Python-ში
python -c "import kapanadze_mathtools; print(kapanadze_mathtools.__version__)"

# 3. ან ეწვიე
https://pypi.org/project/kapanadze-mathtools/
```

წარმატებები! 🎓
