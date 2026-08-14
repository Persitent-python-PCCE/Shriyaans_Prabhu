from config.db import DataBase
class UserDAO:

    def __init__(self):
        self.db = DataBase()
    def create_customer(
        self,
        name,
        email,
        password_hash,
        contact_name=None,
        address=None,
        city=None,
        postal_code=None,
        country=None
    ):
        connection = self.db.connect()

        if connection is None:
            return None

        cursor = connection.cursor()

        try:
            query = """
                INSERT INTO customers
                (
                    CustomerName,
                    Email,
                    PasswordHash,
                    ContactName,
                    Address,
                    City,
                    PostalCode,
                    Country
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                name,
                email,
                password_hash,
                contact_name,
                address,
                city,
                postal_code,
                country
            )

            cursor.execute(query, values)
            connection.commit()

            return cursor.lastrowid

        except Exception as e:
            connection.rollback()
            print(f"Error creating customer: {e}")
            return None

        finally:
            cursor.close()
            connection.close()

    def create_admin(self, name, email, password_hash):
        connection = self.db.connect()

        if connection is None:
            return None

        cursor = connection.cursor()

        try:
            query = """
                INSERT INTO admins
                (
                    AdminName,
                    Email,
                    PasswordHash
                )
                VALUES (%s, %s, %s)
            """

            values = (
                name,
                email,
                password_hash
            )

            cursor.execute(query, values)
            connection.commit()

            return cursor.lastrowid

        except Exception as e:
            connection.rollback()
            print(f"Error creating admin: {e}")
            return None

        finally:
            cursor.close()
            connection.close()

    def get_user_by_email(self, email):
        connection = self.db.connect()

        if connection is None:
            return None

        cursor = connection.cursor(dictionary=True)

        try:
            query = """
                SELECT
                    CustomerID AS user_id,
                    'CUSTOMER' AS role_name,
                    CustomerName AS name,
                    Email AS email,
                    PasswordHash AS password_hash,
                    ContactName AS contact_name,
                    Address AS address,
                    City AS city,
                    PostalCode AS postal_code,
                    Country AS country
                FROM customers
                WHERE Email = %s

                UNION ALL

                SELECT
                    AdminID AS user_id,
                    'ADMIN' AS role_name,
                    AdminName AS name,
                    Email AS email,
                    PasswordHash AS password_hash,
                    NULL AS contact_name,
                    NULL AS address,
                    NULL AS city,
                    NULL AS postal_code,
                    NULL AS country
                FROM admins
                WHERE Email = %s

                LIMIT 1
            """

            cursor.execute(query, (email, email))
            return cursor.fetchone()

        except Exception as e:
            print(f"Error fetching user: {e}")
            return None

        finally:
            cursor.close()
            connection.close()
    
 
    def get_user_by_name(self,name):
        connection = self.db.connect()
        
        if connection is None:
            return None
        
        cursor = connection.cursor(dictionary=True)
        
        try:
            query = """
                SELECT
                    CustomerID AS user_id,
                    'CUSTOMER' AS role_name,
                    CustomerName AS name,
                    Email AS email,
                    PasswordHash AS password_hash,
                    ContactName AS contact_name,
                    Address AS address,
                    City AS city,
                    PostalCode AS postal_code,
                    Country AS country
                FROM customers
                WHERE CustomerName = %s
        
                UNION ALL
        
                SELECT
                    AdminID AS user_id,
                    'ADMIN' AS role_name,
                    AdminName AS name,
                    Email AS email,
                    PasswordHash AS password_hash,
                    NULL AS contact_name,
                    NULL AS address,
                    NULL AS city,
                    NULL AS postal_code,
                    NULL AS country
                FROM admins
                WHERE AdminName = %s
        
                LIMIT 1
            """
        
            cursor.execute(query, (name, name))
            return cursor.fetchone()
        
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None
        
        finally:
            cursor.close()
            connection.close()
 
    def get_user_by_id(self, user_id, role=None):
        connection = self.db.connect()

        if connection is None:
            return None

        cursor = connection.cursor(dictionary=True)

        try:
            if role and role.upper() == "ADMIN":
                query = """
                    SELECT
                        AdminID AS user_id,
                        'ADMIN' AS role_name,
                        AdminName AS name,
                        Email AS email,
                        PasswordHash AS password_hash,
                        NULL AS contact_name,
                        NULL AS address,
                        NULL AS city,
                        NULL AS postal_code,
                        NULL AS country
                    FROM admins
                    WHERE AdminID = %s
                """
                cursor.execute(query, (user_id,))
                return cursor.fetchone()

            if role and role.upper() == "CUSTOMER":
                query = """
                    SELECT
                        CustomerID AS user_id,
                        'CUSTOMER' AS role_name,
                        CustomerName AS name,
                        Email AS email,
                        PasswordHash AS password_hash,
                        ContactName AS contact_name,
                        Address AS address,
                        City AS city,
                        PostalCode AS postal_code,
                        Country AS country
                    FROM customers
                    WHERE CustomerID = %s
                """
                cursor.execute(query, (user_id,))
                return cursor.fetchone()
            query = """
                SELECT
                    CustomerID AS user_id,
                    'CUSTOMER' AS role_name,
                    CustomerName AS name,
                    Email AS email,
                    PasswordHash AS password_hash,
                    ContactName AS contact_name,
                    Address AS address,
                    City AS city,
                    PostalCode AS postal_code,
                    Country AS country
                FROM customers
                WHERE CustomerID = %s

                UNION ALL

                SELECT
                    AdminID AS user_id,
                    'ADMIN' AS role_name,
                    AdminName AS name,
                    Email AS email,
                    PasswordHash AS password_hash,
                    NULL AS contact_name,
                    NULL AS address,
                    NULL AS city,
                    NULL AS postal_code,
                    NULL AS country
                FROM admins
                WHERE AdminID = %s

                LIMIT 1
            """

            cursor.execute(query, (user_id, user_id))
            return cursor.fetchone()

        except Exception as e:
            print(f"Error fetching user: {e}")
            return None

        finally:
            cursor.close()
            connection.close()
 
    def get_all_users(self):
        connection = self.db.connect()

        if connection is None:
            return []

        cursor = connection.cursor(dictionary=True)

        try:
            query = """
                SELECT
                    CustomerID AS user_id,
                    'CUSTOMER' AS role_name,
                    CustomerName AS name,
                    Email AS email,
                    ContactName AS contact_name,
                    Address AS address,
                    City AS city,
                    PostalCode AS postal_code,
                    Country AS country
                FROM customers

                UNION ALL

                SELECT
                    AdminID AS user_id,
                    'ADMIN' AS role_name,
                    AdminName AS name,
                    Email AS email,
                    NULL AS contact_name,
                    NULL AS address,
                    NULL AS city,
                    NULL AS postal_code,
                    NULL AS country
                FROM admins

                ORDER BY user_id
            """

            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Error fetching users: {e}")
            return []

        finally:
            cursor.close()
            connection.close()
    def update_user(
        self,
        user_id,
        role,
        name,
        email,
        contact_name=None,
        address=None,
        city=None,
        postal_code=None,
        country=None
    ):
        connection = self.db.connect()

        if connection is None:
            return False

        cursor = connection.cursor()

        try:
            if role.upper() == "ADMIN":
                query = """
                    UPDATE admins
                    SET
                        AdminName = %s,
                        Email = %s
                    WHERE AdminID = %s
                """

                values = (
                    name,
                    email,
                    user_id
                )

            else:
                query = """
                    UPDATE customers
                    SET
                        CustomerName = %s,
                        Email = %s,
                        ContactName = %s,
                        Address = %s,
                        City = %s,
                        PostalCode = %s,
                        Country = %s
                    WHERE CustomerID = %s
                """

                values = (
                    name,
                    email,
                    contact_name,
                    address,
                    city,
                    postal_code,
                    country,
                    user_id
                )

            cursor.execute(query, values)
            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:
            connection.rollback()
            print(f"Error updating user: {e}")
            return False

        finally:
            cursor.close()
            connection.close()
            
    def delete_user(self, user_id, role):
        connection = self.db.connect()

        if connection is None:
            return False

        cursor = connection.cursor()

        try:
            if role.upper() == "ADMIN":
                query = """
                    DELETE FROM admins
                    WHERE AdminID = %s
                """
            else:
                query = """
                    DELETE FROM customers
                    WHERE CustomerID = %s
                """

            cursor.execute(query, (user_id,))
            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:
            connection.rollback()
            print(f"Error deleting user: {e}")
            return False

        finally:
            cursor.close()
            connection.close()