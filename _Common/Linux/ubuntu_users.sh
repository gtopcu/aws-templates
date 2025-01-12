#!/bin/bash

show_user_info() {
    local username=$1
    echo "User Information for: $username"
    echo "------------------------"
    echo "Groups: $(groups $username)"
    echo "Home Directory: $(getent passwd $username | cut -d: -f6)"
    echo "Shell: $(getent passwd $username | cut -d: -f7)"
    echo "UID: $(id -u $username)"
    echo "Primary GID: $(id -g $username)"
}

show_user_info $1

# Usage
# sh ubuntu_users.sh gtopcu