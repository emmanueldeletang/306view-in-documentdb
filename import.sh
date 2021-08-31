mongoimport --ssl --host MYCLUSTER.docdb.amazonaws.com:27017 --sslCAFile ../rds-combined-ca-bundle.pem --username USER --password XXXX --db vue --type csv --headerline --file c1.csv

mongoimport --ssl --hos tMYCLUSTER.docdb.amazonaws.com:27017 --sslCAFile ../rds-combined-ca-bundle.pem --username USER --password XXXX -d vue c2.json

mongoimport --ssl --host MYCLUSTER.eu-west-3.docdb.amazonaws.com:27017 --sslCAFile ../rds-combined-ca-bundle.pem --username USER --password XXXX -d vue c3.json
