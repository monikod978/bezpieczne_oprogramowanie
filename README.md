# Python demo
Instalacja:
  python -m venv .venv && . .venv/bin/activate
  pip install -r requirements.txt
Skan:
  snyk test --file=requirements.txt --package-manager=pip
