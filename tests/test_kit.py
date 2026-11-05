import tempfile
import unittest
from pathlib import Path
from subprocess import run

ROOT = Path(__file__).resolve().parent.parent

class TestKit(unittest.TestCase):
    def test_skill_names_and_files(self):
        for name in ('task-intake', 'task-build', 'task-optimize', 'task-verify', 'data-audit', 'rule-analysis'):
            p = ROOT / 'agents' / 'skills' / name / 'SKILL.md'
            self.assertTrue(p.is_file(), name)
            self.assertIn('name: ' + name, p.read_text(encoding='utf8'))

    def test_dryrun_apply_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            cmd = ['python3', str(ROOT / 'tools' / 'install.py'), '--target', d]
            dry = run(cmd, capture_output=True, text=True)
            self.assertEqual(0, dry.returncode, dry.stderr)
            self.assertIn('PLAN:', dry.stdout)
            self.assertFalse((Path(d) / 'agents').exists())
            apply = run(cmd + ['--apply'], capture_output=True, text=True)
            self.assertEqual(0, apply.returncode, apply.stderr)
            self.assertTrue((Path(d) / 'agents' / 'skills' / 'task-optimize' / 'SKILL.md').is_file())
            again = run(cmd + ['--apply'], capture_output=True, text=True)
            self.assertEqual(0, again.returncode, again.stderr)
            self.assertIn('SKIP existing:', again.stdout)

    def test_no_overwrite_existing_agents(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / 'AGENTS.md'
            path.write_text('DO NOT CHANGE', encoding='utf8')
            cmd = ['python3', str(ROOT / 'tools' / 'install.py'), '--target', d, '--include-agents', '--apply']
            r = run(cmd, capture_output=True, text=True)
            self.assertEqual(0, r.returncode, r.stderr)
            self.assertEqual('DO NOT CHANGE', path.read_text(encoding='utf8'))

if __name__ == '__main__':
    unittest.main()


class TestReadableAndPaths(unittest.TestCase):
    def test_no_hidden_agents_path(self):
        self.assertFalse((ROOT / '.agents').exists())
        for p in (ROOT / 'START_HERE.md', ROOT / 'PROMPTS.md', ROOT / 'tools' / 'install.py'):
            self.assertNotIn('.agents/skills',p.read_text(encoding='utf8'),str(p))

    def test_verify_includes_requested_checks(self):
        s = (ROOT / 'agents' / 'skills' / 'task-verify' / 'SKILL.md').read_text(encoding='utf8')
        for term in ('입력','중간값','경계','실패','독립 검산','목적함수','제약','미확인','체크리스트'):
            self.assertIn(term,s)
