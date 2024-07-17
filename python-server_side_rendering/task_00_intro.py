#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    # Vérification des types d'entrée
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Gestion des entrées vides
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Processus de chaque invité
    for i, attendee in enumerate(attendees, start=1):
        output_content = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key, 'N/A') or 'N/A'
            output_content = output_content.replace(f'{{{key}}}', value)

        # Génération du fichier de sortie
        output_filename = f'output{i}.txt'
        with open(output_filename, 'w') as file:
            file.write(output_content)

        print(f'Generated {output_filename}')
