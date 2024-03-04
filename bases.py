import sqlite3
import hashlib
import secrets

class DataBase:
    """Classe para lidar com operações de banco de dados."""

    def __init__(self, name='System.db') -> None:
        """
        Inicializa a classe DataBase.

        Args:
            name (str): Nome do arquivo do banco de dados.
        """
        self.name = name
        self.connection = None

    def connect_(self):
        """Conecta ao banco de dados."""
        try:
            self.connection = sqlite3.connect(self.name)
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to connect to the database: {e}")

    def close_connection(self):
        """Fecha a conexão com o banco de dados."""
        try:
            if self.connection:
                self.connection.close()
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to close the database connection: {e}")

    def create_table_users(self):
        """Cria a tabela 'users' no banco de dados, se ela não existir."""
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        user TEXT UNIQUE NOT NULL,
                        password_salt TEXT NOT NULL,
                        password_hash TEXT NOT NULL,
                        access TEXT NOT NULL
                    );
                ''')
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to create users table: {e}")

    def insert_user(self, name, user, password, access):
        """
        Insere um novo usuário na tabela 'users'.

        Args:
            name (str): Nome do usuário.
            user (str): Nome de usuário.
            password (str): Senha do usuário.
            access (str): Nível de acesso do usuário ('Admin' ou 'User').
        """
        # Validating input data
        if not all([name, user, password, access]):
            raise ValueError('All fields are required.')

        # Generating salt
        salt = secrets.token_hex(16)

        # Salting and hashing the password
        hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()

        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute('''
                    INSERT INTO users(name, user, password_salt, password_hash, access) VALUES(?,?,?,?,?)            
                ''', (name, user, salt, hashed_password, access))
                self.connection.commit()
        except sqlite3.IntegrityError:
            raise ValueError('User already exists.')
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to insert user: {e}")

    def check_user(self, user, password):
        """
        Verifica se um usuário existe na tabela 'users' e retorna seu nível de acesso.

        Args:
            user (str): Nome de usuário.
            password (str): Senha do usuário.

        Returns:
            str: Nível de acesso do usuário ('Admin', 'User' ou 'Access denied').
        """
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute('SELECT * FROM users WHERE user = ?', (user,))
                user_data = cursor.fetchone()
                if user_data:
                    salt = user_data[3]
                    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
                    if hashed_password == user_data[4]:
                        return user_data[5]
                return "Access denied"
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to check user: {e}")

    def insert_data(self, full_dataset):

        cursor = self.connection.cursor()

        table_fields = ('nfe', 'serial', 'date_issue', 'key', 'cnpj_issuer','name_issuer', 'value_nfe', 'item_note', 'cod', 'amount', 'description','unit_measurement', 'production_value', 'date_import', 'user', 'date_output')

        amount = ','.join(map(str, '?'*16))
        query = f'''INSERT INTO Notas {table_fields} VALUES ({amount})'''

        try:
            for nota in full_dataset:
                cursor.execute(query, tuple(nota))
                self.connection.commit()
        except sqlite3.IntegrityError:
            print('This note already exists in the database')

    def create_table_nfe(self):
        cursor = self.connection.cursor()
        cursor.execute(f'''

            CREATE TABLE IF NOT EXISTS Notas(
                       
            nfe TEXT,
            serial TEXT,
            date_issue TEXT,
            key TEXT,
            cnpj_issuer TEXT,
            name_issuer TEXT,
            value_nfe TEXT,
            item_note TEXT,
            cod TEXT,
            amount TEXT,
            description TEXT,
            unit_measurement TEXT,
            production_value TEXT,
            date_import TEXT,
            user TEXT,
            date_output TEXT,          
                         
            PRIMARY KEY(key, nfe, item_note)

            );

        ''')

    def update_storage(self, date_output, user, notes):
        try:
            cursor = self.connection.cursor()
            for note in notes:
                cursor.execute(f"""UPDATE Notas SET date_output = "{date_output}",
                                user ='{user}' WHERE nfe = '{note}'""")
                self.connection.commit()
        except AttributeError:
            print('Connect to change fields.')
    
    def update_refund(self, notes):
        try:
            cursor = self.connection.cursor()
            for note in notes:
                cursor.execute(f"UPDATE Notas SET date_output = '' WHERE nfe = '{note}'"
                    )
                self.connection.commit()
        except AttributeError:
            print('Connect to change fields.')

if __name__ == '__main__':
    db = DataBase()
    db.connect_()
    db.create_table_users()
    db.create_table_nfe()
    db.close_connection()
