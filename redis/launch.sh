#!/bin/sh

PASSWORD=$(cat /etc/redis-passwd/passwd)

if [ "${HOSTNAME}" == "redis-0" ]; then
  redis-server --requirepass "${PASSWORD}"
else
  redis-server --slaveof redis-0.redis.default.svc.cluster.local 6379 --masterauth "${PASSWORD}" --requirepass "${PASSWORD}"
fi