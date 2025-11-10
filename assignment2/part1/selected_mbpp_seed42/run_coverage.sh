#!/bin/bash
# Run pytest with coverage for each directory separately

cd "$(dirname "$0")"

for dir in 54_*; do
    if [ -d "$dir" ] && [ -f "$dir/tests.py" ]; then
        echo "=========================================="
        echo "Testing $dir"
        echo "=========================================="
        python3 -m pytest --import-mode=importlib \
            --cov="$dir" \
            --cov-report=term-missing \
            "$dir/tests.py" -v
        echo ""
    fi
done

