#!/usr/bin/python3


import os


def generate_invitations(template, attendees):
    try:
        # Vérifier que le modèle est une chaîne de caractères
        if not isinstance(template, str):
            raise ValueError("Template is not a string")

        # Vérifier que les participants sont une liste de dictionnaires
        if not isinstance(attendees, list) or not all(isinstance(att, dict)
                                                      for att in attendees):
            raise ValueError("Attendees sould be list of dictionnaries")

        # Vérifier que le modèle n'est pas vide
        if template.strip() == "":
            print("Template is empty, no output files generated")
            return

        # Vérifier que la liste des participants n'est pas vide
        if not attendees:
            print("No data prvided, no output file generated")
            return

        # Traiter chaque participant
        for i, attendee in enumerate(attendees, start=1):
            # Remplacer les valeurs manquantes par "N/A"
            name = attendee.get("name", "N/A")
            event_title = attendee.get("event_title", "N/A")
            event_date = attendee.get("event_date", "N/A")
            event_location = attendee.get("event_location", "N/A")

        # Remplacer les espaces réservés par les valeurs du dictionnaire
            invitation = template.format(
                name=name,
                event_title=event_title,
                event_date=event_date if event_date else "N/A",
                event_location=event_location
            )

            # Nommer le fichier de sortie
            output_filename = "output_{}.txt".format(i)

            # Écrire le contenu dans le fichier de sortie
            try:
                with open(output_filename, 'w') as output_file:
                    output_file.write(invitation)
                print("Generated {}".format(output_filename))
            except IOError as e:
                print("Error writing file {}: {}".format(output_filename, e))
    except ValueError as e:
        print("{ValueError: {}".format(e))
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))
