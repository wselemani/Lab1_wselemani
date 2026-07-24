#!/usr/bin/env bash

ARCHIVE_DIR="archive"
SOURCE_FILE="grades.csv"
LOG_FILE="organizer.log"

if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir -p "$ARCHIVE_DIR"
    echo "Directory '$ARCHIVE_DIR' created."
fi

if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: '$SOURCE_FILE' does not exist in the current directory."
    exit 1
fi

TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

ARCHIVED_NAME="grades_${TIMESTAMP}.csv"
ARCHIVED_PATH="${ARCHIVE_DIR}/${ARCHIVED_NAME}"

mv "$SOURCE_FILE" "$ARCHIVED_PATH"

echo "assignment,group,score,weight" > "$SOURCE_FILE"

echo "[${TIMESTAMP}] Archived '${SOURCE_FILE}' -> '${ARCHIVED_PATH}'" >> "$LOG_FILE"

echo "Archiving complete! Process logged to '$LOG_FILE'."

