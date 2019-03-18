# cdvplusplus
## Dependencies
Use `install -r requirements.txt` to install the required dependencies for this project
## Database
You have to provide a valid uri, username and password to use the neo4j driver in this application.

The file has to be created in the root folder of the db module with the name `properties.json` and has to contain the following structure:
`{
	"uri" : "bolt://user:db@localhost:7687",
	"user" : "user",
	"password" : "password"
}`