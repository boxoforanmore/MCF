#!/bin/bash
echo
echo "Running mongod --config /conf/mongo.conf"
echo "With the following configurations"
cat ./conf/mongo.conf
echo
echo
mongod --config /conf/mongo.conf
echo
exit 0
