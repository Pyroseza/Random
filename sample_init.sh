#!/bin/bash
case $1 in
  start)
    sudo /home/pi/unicorn-hat/examples/binary_clock.py 1>/dev/null 2>&1 &
    echo $! > /tmp/binary_clock.pid
    exit 0
    ;;
  stop)
    if [ -f /tmp/binary_clock.pid ]; then
      sudo kill `cat /tmp/binary_clock.pid`
      rm /tmp/binary_clock.pid
      sleep 1
      sudo /home/pi/unicorn-hat/examples/clean.py 1>/dev/null 2>&1
    else
      echo No pid file exists, showing process list
      ps -ef | grep "binary_clock.py"
    fi
    exit 0
    ;;
  restart|force-reload)
    $0 stop
    sleep 1
    $0 start
    ;;
  status)
    if [ -f /tmp/binary_clock.pid ]
    then
      ps -p `cat /tmp/binary_clock.pid`
    else
      echo No pid file exists, showing process list
      ps -ef | grep binary_clock.py
    fi
    ;;
  *)
    echo "Usage: $0 {start|stop|restart|force-reload|status}" >&2
    exit 1
    ;;
esac

exit 0
