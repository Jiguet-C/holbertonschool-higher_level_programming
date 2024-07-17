#!/usr/bin/python3

import sqlite3


def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Création de la table Products si elle n'existe pas encore
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Insertion de données initiales
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    # Valider et fermer la connexion
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
