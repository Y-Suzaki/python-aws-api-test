#!/bin/bash

echo "Start"

ROUTE53_NAME=`yq -r ".Route53.Name" config.yaml`
ROUTE53_ID=`yq -r ".Route53.ID" config.yaml`
echo ${ROUTE53_NAME}
echo ${ROUTE53_ID}
echo "********"

