#!/bin/bash
existe=$(ifconfig tun0 > /dev/null 2>&1 || echo no)
if [ "$existe" = "no" ]; then
  sudo openvpn --daemon --config ./assets/elshaio-rpi4.ovpn
  sleep 6
  for i in {1..50} 
  do 
    sleep 1 && nc -w 2 -z api.telegram.org 443 && break
  done
  sleep 3
  echo VPN encendida
else
  echo Ya existe la VPN
fi

