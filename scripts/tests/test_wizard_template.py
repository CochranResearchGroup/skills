import os
from pathlib import Path
import shlex
import subprocess
import tempfile
import unittest

TEMPLATE = Path(__file__).resolve().parents[2] / "skills/engineering/wizard/template.sh"

class WizardBehavior(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.library = self.root / "library.sh"
        text = TEMPLATE.read_text()
        self.library.write_text(text.split("# STAGES: author this section.", 1)[0])

    def run_bash(self, body, stdin=""):
        return subprocess.run(["bash", "-c", "source " + shlex.quote(str(self.library)) + "\n" + body], cwd=self.root, input=stdin, text=True, capture_output=True, check=True)

    def test_special_value_roundtrip_and_idempotence(self):
        value = "O'Brien $HOME `literal` $(literal) slash\\ end"
        self.run_bash("write_env VALUE " + shlex.quote(value) + "\nwrite_env VALUE " + shlex.quote(value) + '\n[[ "$VALUE" == ' + shlex.quote(value) + ' ]]\n[[ "$(_existing VALUE)" == ' + shlex.quote(value) + ' ]]')
        env = self.root / ".env"
        self.assertEqual(env.stat().st_mode & 0o777, 0o600)
        self.assertEqual(len(env.read_text().splitlines()), 1)
        self.run_bash('ask VALUE "repeat"\n[[ "$VALUE" == ' + shlex.quote(value) + ' ]]', "\n")

    def test_symlink_target_and_mode_survive(self):
        target = self.root / "actual.env"
        target.write_text("KEEP=old\n")
        target.chmod(0o640)
        (self.root / ".env").symlink_to(target)
        self.run_bash("write_env VALUE safe")
        self.assertTrue((self.root / ".env").is_symlink())
        self.assertEqual(target.stat().st_mode & 0o777, 0o640)
        self.assertIn("KEEP=old", target.read_text())
        self.assertIn("VALUE='safe'", target.read_text())

    def test_eof_fails_visible_and_secret_prompts(self):
        self.run_bash('if ask VALUE prompt < /dev/null; then exit 42; fi\nif ask_secret VALUE prompt < /dev/null; then exit 43; fi')

    def test_plain_double_quote_and_unsafe_default(self):
        (self.root / ".env").write_text('PLAIN="simple value"\nUNSAFE="$HOME"\n')
        self.run_bash('[[ "$(_existing PLAIN)" == "simple value" ]]\nif _existing UNSAFE; then exit 44; fi')

    def test_failed_opener_is_reported_without_browser(self):
        # Function shadows the host opener, preventing any real browser effect.
        output = self.run_bash('wslview() { return 1; }\nopen_url https://example.invalid').stdout
        self.assertIn("couldn't open a browser", output)

if __name__ == "__main__":
    unittest.main()
