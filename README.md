# Allgäuer Baufachkongress 2026 – Teilnehmer-App

Web-App für den Allgäuer Baufachkongress. Läuft als einzelne HTML-Datei – kein Backend, keine Datenbank nötig.

## 🔗 Live-Demo (GitHub Pages)

Nach dem Aktivieren von GitHub Pages erreichbar unter:  
`https://DEIN-USERNAME.github.io/bfk-app/`

## 📁 Struktur

```
bfk-app/
├── index.html          ← Die komplette App
├── teilnehmer.json     ← Teilnehmerdaten (aus CSV generiert)
├── scripts/
│   └── csv_to_json.py  ← CSV → JSON Konverter
└── README.md
```

## ✨ Features

- **Login** per Ticketnummer + Nachname
- **Programm** – 3-Tages-Übersicht mit persönlichen Sessions
- **Mein Plan** – individueller Zeitplan je Teilnehmer
- **Netzwerk** – Teilnehmerliste durchsuchen, Kontakt per E-Mail
- **Profil** – Firma, Position, Kontaktdaten hinterlegen
- **Info** – Venue, WLAN, Anreise, Kongressbüro

## 🚀 Deployment

### Option 1: GitHub Pages (empfohlen zum Testen)
1. Repository auf GitHub anlegen
2. Code pushen
3. Settings → Pages → Branch: `main` → Ordner: `/ (root)`
4. App ist live unter `https://USERNAME.github.io/bfk-app/`

### Option 2: Eigener Server / baufachkongress.com/app
1. Ordner `app/` auf dem Server anlegen
2. `index.html` und `teilnehmer.json` hochladen
3. Fertig – keine weitere Konfiguration nötig

## 👥 Teilnehmerdaten aktualisieren

1. CSV-Datei vorbereiten (Format siehe unten)
2. Python-Skript ausführen:
```bash
cd scripts
python3 csv_to_json.py ../teilnehmer.csv ../teilnehmer.json
```
3. `teilnehmer.json` hochladen – fertig

### CSV-Format
```csv
ticket,nachname,vorname,firma,position,branche,email,tel,web,sessions
BFK2026-1001,Müller,Klaus,Baustoff Müller GmbH,Geschäftsführer,Handel,k.mueller@firma.de,+49 89 123,www.firma.de,"0,3,6"
```

## 🔑 Demo-Zugänge

| Ticket | Nachname | Branche |
|--------|----------|---------|
| BFK2026-1001 | Müller | Handel |
| BFK2026-1002 | Schmidt | Handwerk |
| BFK2026-1003 | Weber | Architektur |

## 🛠 Lokale Entwicklung

Einfach `index.html` im Browser öffnen – oder lokalen Server starten:
```bash
python3 -m http.server 8080
# → http://localhost:8080
```
