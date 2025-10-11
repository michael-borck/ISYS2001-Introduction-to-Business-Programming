import os
import sys
import re
import argparse
import glob

# --- US to Australian/British Spelling Mapping ---
# This dictionary contains common American spellings as keys
# and their Australian/British equivalents as values.
# All keys and values are lowercase for consistent lookup.
#
# IMPORTANT: This list prioritizes common and relatively unambiguous conversions.
# Words that have different meanings or usage contexts (e.g., "check" vs "cheque",
# "practice" noun vs "practise" verb) are generally avoided or handled carefully
# to prevent incorrect replacements without deeper linguistic analysis.
#
# Feel free to expand this list with more words relevant to your content.
# Consider adding specific Australian terms if your LLM might generate US equivalents.
US_TO_AU_GB_MAP = {
    # -or to -our
    'color': 'colour',
    'flavor': 'flavour',
    'honor': 'honour',
    'labor': 'labour',
    'neighbor': 'neighbour',
    'ardor': 'ardour',
    'candor': 'candour',
    'clamor': 'clamour',
    'demeanor': 'demeanour',
    'endeavor': 'endeavour',
    'fervor': 'fervour',
    'feverish': 'feverish', # No change, but good to note
    'glamor': 'glamour',
    'harbor': 'harbour',
    'humor': 'humour',
    'odor': 'odour',
    'pajamas': 'pyjamas',
    'parlor': 'parlour',
    'rancor': 'rancour',
    'rigor': 'rigour',
    'savor': 'savour',
    'splendor': 'splendour',
    'vapor': 'vapour',
    'valor': 'valour',

    # -ize to -ise
    'apologize': 'apologise',
    'capitalize': 'capitalise',
    'categorize': 'categorise',
    'centralize': 'centralise',
    'civilize': 'civilise',
    'customize': 'customise',
    'demoralize': 'demoralise',
    'emphasize': 'emphasise',
    'initialize': 'initialise',
    'legalize': 'legalise',
    'materialize': 'materialise',
    'maximize': 'maximise',
    'minimize': 'minimise',
    'modernize': 'modernise',
    'organize': 'organise',
    'oxidize': 'oxidise',
    'patronize': 'patronise',
    'prioritize': 'prioritise',
    'realize': 'realise',
    'recognize': 'recognise',
    'standardize': 'standardise',
    'sympathize': 'sympathise',
    'synthesize': 'synthesise',
    'terrorize': 'terrorise',
    'utilize': 'utilise',
    'victimize': 'victimise',

    # -yze to -yse
    'analyze': 'analyse',
    'paralyze': 'paralyse',
    'catalyze': 'catalyse',

    # -er to -re
    'center': 'centre',
    'fiber': 'fibre',
    'liter': 'litre',
    'meter': 'metre',
    'saber': 'sabre',
    'somber': 'sombre',
    'theater': 'theatre',
    'caliber': 'calibre',
    'lister': 'listre', # lustre
    'meager': 'meagre',

    # -og to -ogue
    'analog': 'analogue',
    'catalog': 'catalogue',
    'dialog': 'dialogue',
    'monolog': 'monologue',
    'epilog': 'epilogue',
    'prolog': 'prologue',

    # -ence to -ense (often swapped, but AU/GB prefers -ence for nouns)
    'defense': 'defence',
    'offense': 'offence',
    'license': 'licence', # noun, verb is 'license' in both
    'pretense': 'pretence',

    # Other common differences
    'aluminum': 'aluminium',
    'apophthegm': 'apophthegm', # Unchanged, but common
    'artifact': 'artefact',
    'ax': 'axe',
    'canceled': 'cancelled',
    'canceling': 'cancelling',
    'counseling': 'counselling',
    'eon': 'aeon',
    'esthetic': 'aesthetic',
    'fetus': 'foetus',
    'fulfill': 'fulfil',
    'fulfillment': 'fulfilment',
    'gray': 'grey',
    'jewelery': 'jewellery',
    'judgement': 'judgment', # AU/GB often uses 'judgment' but 'judgement' also common
    'kerb': 'curb', # US 'curb' -> AU/GB 'kerb'
    'leveled': 'levelled',
    'modeling': 'modelling',
    'mold': 'mould',
    'molding': 'moulding',
    'mustache': 'moustache',
    'omelet': 'omelette',
    'paralytic': 'paralytic',
    'practice': 'practice', # Noun, verb is 'practise' in AU/GB
    'program': 'programme', # as in TV/radio programme, but 'program' for computer program
    'skeptic': 'sceptic',
    'skillful': 'skilful',
    'specialty': 'speciality',
    'storey': 'story', # As in building level (AU/GB 'storey')
    'subpena': 'subpoena', # US 'subpoena' -> AU/GB 'subpoena'
    'traveled': 'travelled',
    'traveling': 'travelling',
    'tire': 'tyre',
    'wagon': 'waggon',
    'whisky': 'whiskey', # AU/GB often uses 'whisky' for Scotch, 'whiskey' for Irish/US
    'woolen': 'woollen',
    'donut': 'doughnut',
    'enroll': 'enrol',
    'enrollment': 'enrolment',
    'instalment': 'installment', # US 'installment' -> AU/GB 'instalment'
    'labeled': 'labelled',
    'labeling': 'labelling',
    'offense': 'offence',
    'defense': 'defence',
    'pretense': 'pretence',
    'license': 'licence', # noun
    'storey': 'story', # storey (level of building) vs story (narrative)
    'acknowledgment': 'acknowledgement',
}


# --- Smart Replacement Function (preserves casing) ---
def smart_replace(match):
    """
    Callback function for re.sub to replace a word while trying to preserve
    the original casing (lowercase, Title Case, UPPERCASE).
    """
    original_word = match.group(0)
    # Look up the British/Australian equivalent in the map (keys are lowercase)
    british_word_lower = US_TO_AU_GB_MAP.get(original_word.lower(), original_word.lower())

    if original_word.islower():
        return british_word_lower
    elif original_word.istitle():
        return british_word_lower.title()
    elif original_word.isupper():
        return british_word_lower.upper()
    else:
        # For mixed case, try to preserve the first letter's case
        if original_word and original_word[0].isupper():
            return british_word_lower.capitalize()
        return british_word_lower


# --- Main Conversion Logic ---
def convert_spelling_in_file(filepath, dry_run=False):
    """
    Converts American spellings to Australian/British in a single Markdown file.
    """
    print(f"Processing: {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Create a combined regex pattern for all words in the map
        # Sort keys by length in descending order to handle cases like 'color' and 'colorful' if they were both in map
        # (Though our current map only has base words, it's a good practice)
        us_words = sorted(US_TO_AU_GB_MAP.keys(), key=len, reverse=True)
        # Use \b for word boundaries to ensure whole word replacement
        # Use re.escape to handle any special characters in the word if they ever appeared in a key
        pattern = r'\b(' + '|'.join(re.escape(word) for word in us_words) + r')\b'
        
        # Perform replacement using the smart_replace function to preserve casing
        new_content = re.sub(pattern, smart_replace, content, flags=re.IGNORECASE)

        if new_content != original_content:
            print("  Changes detected.")
            if dry_run:
                print("  (Dry run) Would have made changes.")
                # You could also print a diff here for a more detailed dry run
                # import difflib
                # diff = difflib.unified_diff(original_content.splitlines(keepends=True),
                #                             new_content.splitlines(keepends=True),
                #                             fromfile='original', tofile='modified')
                # sys.stdout.writelines(diff)
            else:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print("  File updated.")
            return True # Indicates changes were made/would be made
        else:
            print("  No American spellings found to convert.")
            return False # No changes needed

    except FileNotFoundError:
        print(f"Error: File not found - {filepath}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}", file=sys.stderr)
        return False

# --- Command-line Argument Parsing ---
def main():
    parser = argparse.ArgumentParser(
        description="Convert American spellings to Australian/British spellings in Markdown files.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        'paths',
        nargs='+',
        help="One or more file paths, directories, or glob patterns (e.g., 'docs/**/*.md', 'my_file.md', 'my_folder/').\n"
             "If a directory is provided, all .md files within it and its subdirectories will be processed."
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help="Simulate the conversion without writing changes to files. Shows what would be changed."
    )
    parser.add_argument(
        '--add-map',
        metavar='FILE',
        help="Path to an optional custom mapping file (e.g., 'custom_map.txt').\n"
             "Format: 'us_spelling:au_gb_spelling' per line. Ignores lines starting with '#'.\n"
             "Example: 'favourite:favorite' (if you wanted to override default or add new)."
    )

    args = parser.parse_args()

    # Load custom map if provided
    if args.add_map:
        try:
            with open(args.add_map, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if ':' in line:
                            us, au_gb = line.split(':', 1)
                            US_TO_AU_GB_MAP[us.strip().lower()] = au_gb.strip().lower()
                        else:
                            print(f"Warning: Invalid line in custom map '{args.add_map}': '{line}'. Skipping.", file=sys.stderr)
            print(f"Loaded custom mappings from: {args.add_map}")
        except FileNotFoundError:
            print(f"Error: Custom map file '{args.add_map}' not found. Skipping custom map.", file=sys.stderr)
        except Exception as e:
            print(f"Error loading custom map '{args.add_map}': {e}. Skipping custom map.", file=sys.stderr)


    markdown_files = []
    for path_arg in args.paths:
        if os.path.isdir(path_arg):
            for root, _, files in os.walk(path_arg):
                for file in files:
                    if file.endswith('.md'):
                        markdown_files.append(os.path.join(root, file))
        elif '*' in path_arg or '?' in path_arg: # Basic globbing
            markdown_files.extend(glob.glob(path_arg, recursive=True))
        elif os.path.isfile(path_arg) and path_arg.endswith('.md'):
            markdown_files.append(path_arg)
        else:
            print(f"Warning: '{path_arg}' is not a Markdown file or a directory. Skipping.", file=sys.stderr)

    if not markdown_files:
        print("No Markdown files found to process.")
        sys.exit(0)

    total_files_processed = 0
    files_with_changes = 0

    print(f"\n--- Starting Spelling Conversion ({'Dry Run' if args.dry_run else 'Live Run'}) ---")
    print(f"Total files to process: {len(markdown_files)}\n")

    for md_file in sorted(list(set(markdown_files))): # Use set to deduplicate, sort for consistent order
        total_files_processed += 1
        if convert_spelling_in_file(md_file, args.dry_run):
            files_with_changes += 1

    print("\n--- Conversion Summary ---")
    print(f"Files processed: {total_files_processed}")
    print(f"Files with changes (or would have changed in dry run): {files_with_changes}")

    if files_with_changes > 0 and not args.dry_run:
        print("\nConversion completed. Please review the modified files.")
        sys.exit(0) # Exit with 0 even if changes were made, as it was successful conversion
    elif files_with_changes > 0 and args.dry_run:
        print("\nDry run completed. Review the above to see what would have changed. Run without --dry-run to apply changes.")
        sys.exit(0)
    else:
        print("\nNo American spellings found to convert in any files.")
        sys.exit(0) # Success, no changes needed

if __name__ == "__main__":
    main()
