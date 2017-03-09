#!/bin/bash

function prepare() {
    # Delete old container
    docker-compose kill && echo y | docker-compose rm

    # Build images
    docker-compose build

    # Prepare DB
    docker-compose up -d db
    attempt=0
    while [ ${attempt} -le 10 ]; do
        attempt=$(($attempt + 1))
        db_output=$(docker-compose logs db)
        if grep -q 'autovacuum launcher started' <<< ${db_output} ; then
            echo "Postgres is up."
            break
        else
            echo "Waiting for database (attempt: $attempt)"
            sleep 2
        fi
    done
}

function test() {
    # Delete old report
    rm -f coverage.xml xunit.xml

    # Run unit test
    prepare
    docker-compose up test
    docker cp test:/opt/coverage.xml .
    docker cp test:/opt/xunit.xml .
}

function run() {
    prepare
    docker-compose up -d api
}

$@
