#!/usr/bin/bash

# Create the main directory
#mkdir -p AI-Business-Programming-Python

# Change to the main directory
#cd AI-Business-Programming-Python

# Create root-level files
touch README.md syllabus.md weekly-schedule.md study-guide.md

# Create directories for lectures, notebooks, videos, and lab-worksheets
for dir in lectures notebooks videos lab-worksheets; do
    for week in {01..12}; do
        mkdir -p $dir/week$week
    done
done

# Create micro-learning-modules structure
mkdir -p micro-learning-modules/module01/{video,exercises}

# Create course-documents directory and files
mkdir -p course-documents
touch course-documents/{design-choices.md,accessibility-guide.md,technology-setup.md}

# Create .github/workflows directory
mkdir -p .github/workflows

# Display the created structure
tree
