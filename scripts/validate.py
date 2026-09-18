#!/usr/bin/env python3
"""Validate the portable skill package, references and timed example."""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def validate(root):
    errors = []
    skill = (root / 'SKILL.md').read_text(encoding='utf-8')
    match = re.match(r'^---\n(.*?)\n---\n', skill, re.S)
    if not match:
        return ['SKILL.md: missing YAML frontmatter']
    try:
        front = yaml.safe_load(match.group(1))
        ui = yaml.safe_load((root / 'agents/openai.yaml').read_text(encoding='utf-8'))
    except yaml.YAMLError as exc:
        return [f'Invalid YAML: {exc}']
    if not isinstance(front, dict):
        return ['SKILL.md: frontmatter must be a mapping']
    name = front.get('name')
    if name != 'farming-drama-writer':
        errors.append('Unexpected skill name')
    desc = front.get('description')
    if not isinstance(desc, str) or not desc.strip() or len(desc) > 1024:
        errors.append('Missing or invalid description')
    interface = ui.get('interface', {}) if isinstance(ui, dict) else {}
    short = interface.get('short_description', '')
    if not isinstance(short, str) or not 25 <= len(short) <= 64:
        errors.append('short_description must contain 25–64 characters')
    prompt = interface.get('default_prompt', '')
    if not isinstance(prompt, str) or '$farming-drama-writer' not in prompt:
        errors.append('default_prompt must invoke the skill')
    for path in sorted(root.rglob('*.md')):
        text = path.read_text(encoding='utf-8')
        rel = path.relative_to(root)
        if re.search(r'\[TODO:|/Users/[^/\s]+/|/home/[^/\s]+/', text):
            errors.append(f'{rel}: placeholder or machine-specific user path')
        for link in re.findall(r'\]\(([^)]+)\)', text):
            if '://' in link or link.startswith('#'):
                continue
            target = link.split('#', 1)[0]
            resolved = (path.parent / target).resolve()
            if root.resolve() not in resolved.parents or not resolved.is_file():
                errors.append(f'{rel}: invalid local link {link}')
    sample = (root / 'examples/EP001.md').read_text(encoding='utf-8')
    scenes = re.findall(r'^## (EP\d{3}_SC\d{2})[^\n]*约 (\d+) 秒$', sample, re.M)
    if len(scenes) != 4 or len({s[0] for s in scenes}) != len(scenes):
        errors.append('Example needs four uniquely identified timed scenes')
    if sum(int(s[1]) for s in scenes) != 90:
        errors.append('Example scene durations must sum to 90 seconds')
    return errors


if __name__ == '__main__':
    try:
        failures = validate(ROOT)
    except (OSError, UnicodeError) as exc:
        failures = [str(exc)]
    for failure in failures:
        print(f'ERROR: {failure}', file=sys.stderr)
    if failures:
        sys.exit(1)
    print('PASS: skill metadata, references, portability and timed example')
