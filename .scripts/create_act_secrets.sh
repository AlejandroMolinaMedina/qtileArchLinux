#!/bin/bash

echo "Create .secrets file"
grep -oh "secrets.[A-Za-z0-9_]*" .github/workflows/*.yml | cut -d'.' -f2 | sort -u | awk '{print $1"=\"\""}' >.secrets
