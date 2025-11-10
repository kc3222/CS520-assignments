#!/bin/bash
# Run pytest with coverage (line and branch coverage) for each question directory

for dir in question_*/; do
    if [ -d "$dir" ]; then
        echo "============================================================"
        echo "Testing $dir"
        echo "============================================================"
        (cd "$dir" && pytest \
            --import-mode=importlib \
            --cov=. \
            --cov-report=term-missing \
            --cov-branch \
            tests.py \
            -v)
        echo ""
    fi
done
