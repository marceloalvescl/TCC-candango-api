from psycopg2 import connect, DatabaseError, extras
from settings import logger
from utils.constants import DB_SCHEMA, DB_CREDENTIALS
from utils.tools import get_keys

class DataBase:
    def __init__(self):

        try:
            self._db = connect(
                host=DB_CREDENTIALS['DatabaseHost'],
                database=DB_CREDENTIALS['DatabaseName'],
                user=DB_CREDENTIALS['DatabaseUser'],
                password=DB_CREDENTIALS['DatabasePassword']
            )
            self._db.autocommit = False
            self.cursor = self._db.cursor(cursor_factory=extras.DictCursor)
            self._db.commit()
            logger.info("a new database connection")

        except Exception as err:
            logger.fatal("Error connecting to Database")
            logger.fatal(err)

    def handle_execution(self, sql):
        try:
            self.cursor.execute(sql)
            self._db.commit()
        except DatabaseError as error:
            logger.error(f"Problem while trying to execute the script: {sql}")
            logger.error(error)
            self._db.rollback()
            return str(error)
        return self.cursor

    def getAll(self, sql):
        if self._db is not None:
            cursor = self.handle_execution(sql)
            content = cursor.fetchall()
            cursor.close()
            self._db.close()
        else:
            content = 'error'

        return content


    def getOne(self, sql):
        if self._db is not None:
            cursor = self.handle_execution(sql)
            content = cursor.fetchone()
            cursor.close()
            self._db.close()
        else:
            content = 'error'

        return content    

    def insert_new_element(self, sql):
        keys = get_keys(sql)
        if self._db is not None:
            try:
                cursor = self.handle_execution(sql)
                result = cursor.rowcount
                cursor.close()
                self._db.close()
                if result > 0:
                    return True
                else:
                    return False
            except Exception as err:
                logger.fatal(err)
        else:
            return 'error'
        
    def update(self, sql):
        try:
            if self._db is not None:
                cursor = self.handle_execution(sql)
                result = cursor.rowcount
                cursor.close()
                self._db.close()
                if result > 0:
                    return True
                else:
                    return False
            else:
                content = 'error'

            return content
        except Exception as err:
            logger.fatal(err)



