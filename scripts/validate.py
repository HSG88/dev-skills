"""Validate this repo's two-field, plain-scalar skill format and file links."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def validate(root):
    errors = []
    skills = sorted((root / 'skills').glob('*/SKILL.md'))
    if not skills:
        errors.append('No skills found')
    names = set()
    for path in skills:
        text = path.read_text()
        parts = text.split('---\n', 2)
        fields = {}
        if len(parts) != 3 or parts[0]:
            errors.append(f'{path.relative_to(root)}: missing frontmatter')
            continue
        for line in parts[1].splitlines():
            key, separator, value = line.partition(': ')
            if not separator or key in fields:
                errors.append(f'{path.relative_to(root)}: invalid or duplicate field')
            fields[key] = value.strip()
        name = fields.get('name', '')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
            errors.append(f'{path.relative_to(root)}: invalid name')
        if name != path.parent.name or name in names:
            errors.append(f'{path.relative_to(root)}: mismatched or duplicate name')
        names.add(name)
        if set(fields) != {'name', 'description'} or not fields.get('description'):
            errors.append(f'{path.relative_to(root)}: expected name and description')
        if not parts[2].strip():
            errors.append(f'{path.relative_to(root)}: empty body')
    for path in root.rglob('*.md'):
        if '.git' in path.relative_to(root).parts:
            continue
        for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^\s)]+)\)', path.read_text()):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            if not (path.parent / unquote(url.path)).exists():
                errors.append(f'{path.relative_to(root)}: missing link {target}')
    return errors


if __name__ == '__main__':
    failures = validate(Path(__file__).resolve().parents[1])
    print('\n'.join(failures) if failures else 'Skill metadata and local file links are valid.')
    sys.exit(bool(failures))
