#!/bin/bash
sudo pkill openvpn
sleep 3
for i in {1..50}
do
  sleep 1 && nc -w 2 -z api.telegram.org 443 && break
done

