#!/usr/bin/env bash

ARCHIVE_DIR="archive"
SOURCE_FILE="grades.csv"
LOG_FILE="organizer.log"

# 1. Archive Directory Check & Creation
if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir -p "$ARCHIVE_DIR"
    echo "Directory '$ARCHIVE_DIR' created."
fi

# Check if source file exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: '$SOURCE_FILE' does not exist in the current directory."
    exit 1
fi

# 2. Timestamp Generation (Format: YYYYMMDD-HHMMSS)
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

ARCHIVED_NAME="grades_${TIMESTAMP}.csv"
ARCHIVED_PATH="${ARCHIVE_DIR}/${ARCHIVED_NAME}"

# 3. Archival Process: Move and rename original file
mv "$SOURCE_FILE" "$ARCHIVED_PATH"

# 4. Workspace Reset: Immediately create new empty grades.csv
echo "assignment,group,score,weight" > "$SOURCE_FILE"

# 5. Logging: Append record to organizer.log
echo "[${TIMESTAMP}] Archived '${SOURCE_FILE}' -> '${ARCHIVED_PATH}'" >> "$LOG_FILE"

echo "Archiving complete! Process logged to '$LOG_FILE'."
