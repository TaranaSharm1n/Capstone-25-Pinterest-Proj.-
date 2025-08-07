from collections import defaultdict, Counter
from math import log2
import csv
import os

# Define your manual theme data
data = {
    'Participant A': {
        'initial': [
            {'broad': 'hair', 'sub': 'tutorial'},
            {'broad': 'pose', 'sub': ''},
            {'broad': 'fashion', 'sub': 'elegant'},
            {'broad': 'fashion', 'sub': 'acubi'},
        ],
        'day_2': [
            {'broad': 'hair', 'sub': ''},
            {'broad': 'fashion', 'sub': 'acubi'},
            {'broad': 'pose', 'sub': 'overshot'},
            {'broad': 'makeup', 'sub': 'douyin'},
        ],
        'day_3':[
            {'broad': 'pose', 'sub': 'full body'},
            {'broad': 'makeup', 'sub': 'douyin'},
            {'broad': 'hair', 'sub': 'curtain bangs'},
            {'broad': 'fashion', 'sub': 'acubi'},
        ],
        'day_4':[
            {'broad': 'makeup', 'sub': 'douyin'},
            {'broad': 'fashion', 'sub': 'acubi'},
            {'broad': 'hair', 'sub': 'braided updo'},
            {'broad': 'pose', 'sub': 'selfie'},
        ],
        'day_5':[
            {'broad': 'makeup', 'sub': 'douyin'},
            {'broad': 'fashion', 'sub': 'acubi'},
            {'broad': 'pose', 'sub': 'selfie'},
            {'broad': 'hair', 'sub': ''},
        ],
        'day_6':[
            {'broad': 'fashion', 'sub': 'office siren'},
            {'broad': 'hair', 'sub': 'tutorial'},
            {'broad': 'makeup', 'sub': 'douyin'},
            {'broad': 'pose', 'sub': ''},

        ],
        'final':[
            {'broad': 'makeup', 'sub': 'douyin'},
            {'broad': 'pose', 'sub': 'photobooth'},
            {'broad': 'hair', 'sub': 'japanese side bangs'},
            {'broad': 'art', 'sub': ''},
        ]
    },
    'Participant B': {
        'initial': [
            {'broad': 'pose', 'sub': 'overshot'},
            {'broad': 'nails', 'sub': 'summer'},
            {'broad': 'art', 'sub': 'scrapbook'},
            {'broad': 'hellokitty', 'sub': ''},
        ],
        'day_2': [
            {'broad': 'pose', 'sub': 'digital camera'},
            {'broad': 'nails', 'sub': 'gold'},
            {'broad': 'fashion', 'sub': 'coastal'},
            {'broad': 'decor', 'sub': 'soft maximalism'},
        ],
        'day_3': [
            {'broad': 'pose', 'sub': 'digital camera'},
            {'broad': 'jewelery', 'sub': 'beach'},
            {'broad': 'nails', 'sub': 'summer'},
        ],
        'day_4': [
            {'broad': 'pose', 'sub': 'overshot'},
            {'broad': 'jewelry', 'sub': 'keychain'},
            {'broad': 'pose', 'sub': 'digital camera'},
        ],
        'day_5': [
            {'broad': 'pose', 'sub': ''},
            {'broad': 'jewelery', 'sub': ''},
            {'broad': 'nails', 'sub': 'gold'},
            {'broad': 'pose', 'sub': 'digital camera'},
        ],
        'day_6': [
            {'broad': 'fashion', 'sub': 'coastal'},
            {'broad': 'hair', 'sub': ''},
            {'broad': 'decor', 'sub': ''},
            {'broad': 'fashion', 'sub': 'coastal'},
        ],
        'final':[
            {'broad': 'pose', 'sub': 'digital camera'},
            {'broad': 'fashion', 'sub': 'coastal'},
            {'broad': 'nails', 'sub': 'summer'},
            {'broad': 'jewelery', 'sub': 'keychain'},
        ]
    },
'Participant C': {
    'initial': [
        {'broad': 'decor', 'sub': 'minimalist'},
        {'broad': 'fashion', 'sub': 'office siren'},
        {'broad': 'pose', 'sub': 'overshot'},
        {'broad': 'fashion', 'sub': 'alternative'},
        {'broad': 'fashion', 'sub': 'y2k alternative'},
    ],
    'day_2': [
        {'broad': 'hair', 'sub': ''},
        {'broad': 'nails', 'sub': 'alternative'},
        {'broad': 'fashion', 'sub': 'alternative'},
        {'broad': 'makeup', 'sub': 'cool tone'},
    ],
    'day_3': [
        {'broad': 'fashion', 'sub': 'alternative'},
        {'broad': 'decor', 'sub': 'gothic'},
        {'broad': 'fashion', 'sub': 'gothic'},
        {'broad': 'fashion', 'sub': 'gothic'},
    ],
    'day_4': [
        {'broad': 'bunny', 'sub': ''},
        {'broad': 'decor', 'sub': 'layout'},
        {'broad': 'decor', 'sub': 'layout'},
        {'broad': 'fashion', 'sub': 'alternative'},
    ],
    'day_5': [
        {'broad': 'fashion', 'sub': 'alternative'},
        {'broad': 'nails', 'sub': 'alternative'},
        {'broad': 'jewelery', 'sub': 'silver'},
        {'broad': 'decor', 'sub': 'coquette'},
    ],
    'day_6': [
        {'broad': 'pose', 'sub': 'selfie'},
        {'broad': 'phone', 'sub': 'grunge'},
        {'broad': 'pose', 'sub': 'selfie'},
        {'broad': 'videogame', 'sub': ''},
    ],
    'final':[
        {'broad': 'fashion', 'sub': 'gothic'},
        {'broad': 'videogame', 'sub': ''},
        {'broad': 'nails', 'sub': 'alternative'},
        {'broad': 'fashion', 'sub': 'alternative'},
    ],
},
    'Participant D': {
        'initial': [
            {'broad': 'fashion', 'sub': 'grunge'},
            {'broad': 'landscape', 'sub': 'sunset'},
            {'broad': 'minecraft', 'sub': 'building'},
        ],
        'day_2': [
            {'broad': 'landscape', 'sub': 'mountains'},
            {'broad': 'landscape', 'sub': 'sunset'},
            {'broad': 'landscape', 'sub': 'sunlight'},
            {'broad': 'anime', 'sub': ''},
        ],
        'day_3': [
            {'broad': 'minecraft', 'sub': 'building'},
            {'broad': 'cat', 'sub': ''},
            {'broad': 'bedroom', 'sub': 'coquette'},
            {'broad': 'pose', 'sub': 'selfie'},
        ],
        'day_4': [
            {'broad': 'anime', 'sub': ''},
            {'broad': 'hair', 'sub': ''},
            {'broad': 'fashion', 'sub': 'comfortable'},
            {'broad': 'bedroom', 'sub': 'coquette'},
        ],
        'day_5': [
            {'broad': 'minecraft', 'sub': 'building'},
            {'broad': 'car', 'sub': 'LED interior'},
            {'broad': 'hair', 'sub': ''},
            {'broad': 'cat', 'sub': ''},
        ],
        'day_6': [
            {'broad': 'fashion', 'sub': 'vacation'},
            {'broad': 'bedroom', 'sub': 'y2k'},
            {'broad': 'anime', 'sub': ''},
            {'broad': 'car', 'sub': 'LED interior'},
        ],
        'final':[
            {'broad': 'pose', 'sub': 'sitting'},
            {'broad': 'anime', 'sub': ''},
            {'broad': 'cat', 'sub': ''},
            {'broad': 'bedroom', 'sub': 'coquette'},
        ],
    },
        'Participant E': {
            'initial': [
                {'broad': 'hair', 'sub': ''},
                {'broad': 'cat', 'sub': ''},
                {'broad': 'jewelery', 'sub': 'gold bangles'},
                {'broad': 'phone', 'sub': ''},
            ],
            'day_2': [
                {'broad': 'jewelery', 'sub': 'gold bangles'},
                {'broad': 'makeup', 'sub': 'natural'},
                {'broad': 'shoe', 'sub': ''},
                {'broad': 'art', 'sub': 'painting'},
            ],
            'day_3': [
                {'broad': 'makeup', 'sub': 'natural'},
                {'broad': 'fashion', 'sub': 'casual'},
                {'broad': 'phone', 'sub': ''},
                {'broad': 'jewelery', 'sub': 'spring'},
            ],
            'day_4': [
                {'broad': 'makeup', 'sub': 'natural'},
                {'broad': 'jewelery', 'sub': ''},
                {'broad': 'fashion', 'sub': 'casual'},
            ],
            'day_5': [
                {'broad': 'fashion', 'sub': 'culture'},
                {'broad': 'makeup', 'sub': 'natural'},
                {'broad': 'art', 'sub': 'sketch'},
                {'broad': 'art', 'sub': 'sketch'},
            ],
            'day_6': [
                {'broad': 'accessory', 'sub': 'bag'},
                {'broad': 'art', 'sub': 'painting'},
                {'broad': 'gift', 'sub': 'basket'},
                {'broad': 'jewelery', 'sub': 'spring'},
            ],
            'final':[
                {'broad': 'accessory', 'sub': 'bag'},
                {'broad': 'makeup', 'sub': 'lipstick'},
                {'broad': 'gift', 'sub': 'cards'},
                {'broad': 'art', 'sub': 'sketch'},
            ]
    }
}

def calculate_scores(entries, key):
    total = len(entries)
    if total == 0:
        return 0.0, 0.0

    values = [e[key] for e in entries if e[key] != '']
    unique = set(values)
    most_common = Counter(values).most_common(1)

    repetition = 0.0
    if most_common:
        repetition = most_common[0][1] / len(values) * 100 if values else 0.0

    diversity = len(unique) / len(values) * 100 if values else 0.0

    return repetition, diversity

def analyze_data(data):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "theme_frequencies.csv")

    with open(csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Participant', 'Day', 'Broad Repetition (%)', 'Broad Diversity (%)', 'Sub Repetition (%)', 'Sub Diversity (%)'])

        for participant, days in data.items():
            print(f"--- {participant} ---")
            overall_broad = []
            overall_sub = []

            for day, entries in days.items():
                rep_broad, div_broad = calculate_scores(entries, 'broad')
                rep_sub, div_sub = calculate_scores(entries, 'sub')

                print(f"{day}: Broad - Repetition = {rep_broad:.2f}%, Diversity = {div_broad:.2f}%")
                print(f"{day}: Sub   - Repetition = {rep_sub:.2f}%, Diversity = {div_sub:.2f}%")

                writer.writerow([participant, day, f"{rep_broad:.2f}", f"{div_broad:.2f}", f"{rep_sub:.2f}", f"{div_sub:.2f}"])

                overall_broad.extend([entry['broad'] for entry in entries if entry['broad']])
                overall_sub.extend([entry['sub'] for entry in entries if entry['sub']])

            # Overall stats
            rep_broad_total = Counter(overall_broad).most_common(1)[0][1] / len(overall_broad) * 100 if overall_broad else 0.0
            div_broad_total = len(set(overall_broad)) / len(overall_broad) * 100 if overall_broad else 0.0

            rep_sub_total = Counter(overall_sub).most_common(1)[0][1] / len(overall_sub) * 100 if overall_sub else 0.0
            div_sub_total = len(set(overall_sub)) / len(overall_sub) * 100 if overall_sub else 0.0

            print(f"\nOverall for {participant}: Broad - Repetition = {rep_broad_total:.2f}%, Diversity = {div_broad_total:.2f}%")
            print(f"Overall for {participant}: Sub   - Repetition = {rep_sub_total:.2f}%, Diversity = {div_sub_total:.2f}%\n")

analyze_data(data)