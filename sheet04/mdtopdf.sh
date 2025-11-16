#!/bin/bash
# Dieses Skript erstellt pdf Dateien aus Markdown Dateien

i=0
while [ $i -lt 5 ]; do
    INDEX=$(printf "%02d" $i)
    if [ -f sheet"$INDEX".md ]; then
        echo "Konvertiere sheet$INDEX.md zu PDF..."
        pandoc sheet"$INDEX".md -o sheet"$INDEX".pdf
    else
        echo "Datei sheet$INDEX.md nicht gefunden. Beende Konvertierung."
        break
    fi
    i=$((i + 1))
done

echo "Skript beendet."