import sqlite3


class DBProxy:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
                                   CREATE TABLE IF NOT EXISTS dados (
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   nome TEXT NOT NULL,
                                   score INTEGER NOT NULL,
                                   data TEXT NOT NULL)
                                '''
                                )

    def save(self, score_dict: dict):
        print(score_dict)  # Verifique o conteúdo do dicionário
        self.connection.execute('INSERT INTO dados (nome, score, data) VALUES (:name, :score, :data)', score_dict)
        self.connection.commit()

    def retrieve_top10(self) -> list:
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        self.connection.close()