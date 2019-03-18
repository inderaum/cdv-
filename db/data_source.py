from neo4j import GraphDatabase
import json
import os


class DataSource:
    pwd = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):
        properties = self.read_properties()
        self._uri = properties['uri']
        self._user = properties['user']
        self._password = properties['password']
        self._driver = GraphDatabase.driver(self._uri, auth=(self._user, self._password))

    def close(self):
        self._driver.close()

    def print_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    def read_properties(self):
        try:
            db_properties = open(self.pwd + '\\properties.json', 'r')
            return json.loads(db_properties.read())
        except IOError as error:
            print(error)
            exit()

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]
