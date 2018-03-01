ip netns exec "$1" ping6 "$2" -c 1 -n -W 1 -q
