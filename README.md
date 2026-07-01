# pretty

CLI tool to pretty-print JSON and XML files.

## Requirements

Python 3. No external dependencies.

## Usage

```
python3 src/pretty.py -f <input> -o <output>
```

### Options

| Flag | Description |
|------|-------------|
| `-x`, `--xml` | Path to XML file |
| `-j`, `--json` | Path to JSON file |
| `-a`, `--auto` | Autodetect format from file extension |
| `-o`, `--output` | Output file path (required) |
| `-v`, `--verbose` | Enable verbose output |

### Examples

Pretty-print XML:

```
python3 src/pretty.py -x examples/slideshow.xml -o output.xml
```

Pretty-print JSON:

```
python3 src/pretty.py -j examples/example.json -o output.json
```

Auto-detect format by extension:

```
python3 src/pretty.py -a examples/example.json -o output.json
```

## Input / Output

**Input** — files with compact (single-line) or inconsistently formatted content:

```json
{"field1" : "cc11","field2" : "cc22"}
```

```xml
<slideshow><title>Demo slideshow</title><slide><title>Slide title</title></slide></slideshow>
```

**Output** — indented, human-readable content:

```json
{
    "field1": "cc11",
    "field2": "cc22",
    "structField": {
        "sf1": "ccc11",
        "sf2": "ccc22"
    }
}
```

```xml
<?xml version="1.0" ?>
<slideshow>
    <title>Demo slideshow</title>
    <slide>
        <title>Slide title</title>
    </slide>
</slideshow>
```

## Error handling

- Non-existent or unreadable input files exit with code 1 and an error message.
- Unwritable output paths exit with code 1.
- Unrecognized extensions (via `--auto`) exit with code 1.
- Missing required `--output` flag is handled by `argparse`.
