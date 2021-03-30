from psycopg2 import connect, DatabaseError, extras
from settings import logger
from utils.contants import DB_SCHEMA, DB_CREDENTIALS
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

            self._db.close()
        else:
            content = 'error'

        return content


    def getOne(self, sql):
        if self._db is not None:
            cursor = self.handle_execution(sql)
            content = cursor.fetchone()
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
                if result > 0:
                    return True
                else:
                    return False
            except Exception as err:
                logger.fatal(err)
        else:
            return 'error'
        
    def insert(self, sql):
        db_session = self.getDbSession()
        try:
            return db_session.persist(sql)
        except Exception as err:
            logger.fatal(err)



