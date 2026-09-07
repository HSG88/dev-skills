"""Small checks that the validator accepts valid input and rejects broken input."""
from pathlib import Path
from tempfile import TemporaryDirectory
from validate import validate


with TemporaryDirectory() as directory:
    root = Path(directory)
    path = root / 'skills' / 'example' / 'SKILL.md'
    path.parent.mkdir(parents=True)
    valid = '---\nname: example\ndescription: Assess a proposal.\n---\nReview evidence.\n'
    path.write_text(valid)
    assert validate(root) == []
    path.write_text(valid.replace('description: Assess a proposal.', 'description: '))
    assert validate(root)
    path.write_text(valid.replace('name: example', 'name: other'))
    assert validate(root)
    path.write_text(valid.replace('description: Assess a proposal.', 'description: [unterminated'))
    assert validate(root), 'Malformed YAML must not pass'
    path.write_text(valid.replace('description: Assess a proposal.', 'description: []'))
    assert validate(root), 'Description must be a nonempty string'
    path.write_text(valid.replace('name: example', 'name: example\nname: example'))
    assert validate(root), 'Duplicate metadata keys must not pass'
    path.write_text(valid + '\n[Missing](missing.md)\n')
    assert validate(root)
    path.write_text(valid)
    (root / 'README.md').write_text('[Skill](skills/example/SKILL.md)\n[Web](https://example.com)\n')
    assert validate(root) == []
print('Validator checks passed.')
