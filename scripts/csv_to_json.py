#!/usr/bin/env python3
"""
Allgäuer Baufachkongress – CSV zu JSON Konverter
Verwendung: python3 csv_to_json.py teilnehmer.csv teilnehmer.json
"""

import csv
import json
import sys
import os

def csv_to_json(csv_path, json_path):
    teilnehmer = {}

    with open(csv_path, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ticket   = row.get('ticket', '').strip()
            nachname = row.get('nachname', '').strip().lower()

            if not ticket or not nachname:
                continue

            # Sessions als Liste von Integers
            sessions_raw = row.get('sessions', '')
            sessions = []
            if sessions_raw:
                try:
                    sessions = [int(s.strip()) for s in sessions_raw.split(',') if s.strip()]
                except ValueError:
                    sessions = []

            key = f"{ticket}|{nachname}"
            teilnehmer[key] = {
                "id":       ticket,
                "name":     f"{row.get('vorname','').strip()} {row.get('nachname','').strip()}".strip(),
                "ticket":   ticket,
                "mySessions": sessions,
                "profile": {
                    "firma":      row.get('firma', '').strip(),
                    "position":   row.get('position', '').strip(),
                    "branche":    row.get('branche', '').strip(),
                    "email":      row.get('email', '').strip(),
                    "tel":        row.get('tel', '').strip(),
                    "web":        row.get('web', '').strip(),
                    "bio":        row.get('bio', '').strip(),
                    "visNetwork": True,
                    "visEmail":   True
                }
            }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(teilnehmer, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(teilnehmer)} Teilnehmer exportiert → {json_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Verwendung: python3 csv_to_json.py INPUT.csv OUTPUT.json")
        sys.exit(1)

    csv_path = sys.argv[1]
    json_path = sys.argv[2]

    if not os.path.exists(csv_path):
        print(f"❌ Datei nicht gefunden: {csv_path}")
        sys.exit(1)

    csv_to_json(csv_path, json_path)
