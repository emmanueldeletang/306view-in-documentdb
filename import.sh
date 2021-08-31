mongoimport --ssl --host docdbemdel.cluster-cyxxysmikvg5.eu-west-3.docdb.amazonaws.com:27017 --sslCAFile ../rds-combined-ca-bundle.pem --username edesa --password Toto1234 --db vue --type csv --headerline --file c1.csv

mongoimport --ssl --host docdbemdel.cluster-cyxxysmikvg5.eu-west-3.docdb.amazonaws.com:27017 --sslCAFile ../rds-combined-ca-bundle.pem --username edesa --password Toto1234 -d vue c2.json

mongoimport --ssl --host docdbemdel.cluster-cyxxysmikvg5.eu-west-3.docdb.amazonaws.com:27017 --sslCAFile ../rds-combined-ca-bundle.pem --username edesa --password Toto1234  -d vue c3.json
