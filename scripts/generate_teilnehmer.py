import json, re

# PROGRAM array aus index.html – (day, time) -> numeric id
PROGRAM = [
    (0,'10:30',0),(0,'11:30',1),(0,'13:30',2),(0,'13:45',3),(0,'14:30',4),
    (0,'15:00',5),(0,'15:15',6),(0,'16:30',7),(0,'17:00',8),
    (1,'09:00',9),(1,'10:15',10),(1,'10:15',11),(1,'11:15',12),(1,'13:30',13),
    (1,'15:00',14),(1,'15:15',15),(1,'16:00',16),
    (2,'09:30',17),(2,'10:00',18),(2,'10:45',19),(2,'11:00',20),(2,'12:00',21),
]
# (day, time) -> list of ids (mehrere Sessions können gleiche Zeit haben)
session_map = {}
for day, time, sid in PROGRAM:
    session_map.setdefault((day, time), []).append(sid)

data = json.load(open('testdata/teilnehmer_anmeldungen.json', encoding='utf-8'))

users = {}
participants = []

for i, t in enumerate(data):
    tid = t['teilnehmer_id']           # z.B. TN-00001
    nachname = t['nachname'].lower()
    name = t['vorname'] + ' ' + t['nachname']
    key = tid + '|' + nachname

    # Sessions mappen
    my_sessions = []
    for a in t.get('anmeldungen', []):
        if a['status'] != 'bestätigt':
            continue
        pp = a['programmpunkt']
        day = pp['kongresstag'] - 1    # 1-basiert → 0-basiert
        time = pp['startzeit']
        ids = session_map.get((day, time), [])
        for sid in ids:
            if sid not in my_sessions:
                my_sessions.append(sid)

    uid = 'u' + str(i + 1)

    users[key] = {
        'id': uid,
        'name': name,
        'ticket': tid,
        'mySessions': sorted(my_sessions),
        'profile': {
            'firma': t.get('firma', ''),
            'position': t.get('position', ''),
            'branche': t.get('branche', ''),
            'email': t.get('email', ''),
            'tel': t.get('telefon', ''),
            'web': '',
            'bio': '',
            'visNetwork': True,
            'visEmail': True,
        }
    }

    participants.append({
        'id': uid,
        'name': name,
        'firma': t.get('firma', ''),
        'position': t.get('position', ''),
        'branche': t.get('branche', ''),
        'email': t.get('email', ''),
        'visEmail': True,
        'bio': '',
    })

out = 'const USERS=' + json.dumps(users, ensure_ascii=False, indent=None) + ';\n\n'
out += 'const ALL_PARTICIPANTS=' + json.dumps(participants, ensure_ascii=False, indent=None) + ';\n'

with open('teilnehmer.js', 'w', encoding='utf-8') as f:
    f.write(out)

print(f'Fertig: {len(users)} Teilnehmer, {len(participants)} Netzwerk-Einträge')
