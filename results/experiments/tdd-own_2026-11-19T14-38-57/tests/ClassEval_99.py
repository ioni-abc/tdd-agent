import unittest


import unittest

import os

import tempfile

import zipfile

class AgentTest_read_zip_file(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.dir = self._tmp.name

    def _make_zip(self, name="aaa.zip"):
        path = os.path.join(self.dir, name)
        with zipfile.ZipFile(path, "w") as zf:
            zf.writestr("bbb.txt", "hello")
        return path

    def test_read_zip_file_1(self):
        # A valid zip file: read_zip_file returns an open file object (not None)
        path = self._make_zip()
        zfp = ZipFileProcessor(path)
        file = zfp.read_zip_file()
        self.addCleanup(lambda: file.close() if file is not None else None)
        self.assertIsNotNone(file)
        self.assertTrue(hasattr(file, "read"))

    def test_read_zip_file_2(self):
        # The returned file object is open (not closed)
        path = self._make_zip()
        zfp = ZipFileProcessor(path)
        file = zfp.read_zip_file()
        self.addCleanup(lambda: file.close() if file is not None else None)
        self.assertIsNotNone(file)
        self.assertFalse(file.closed)

    def test_read_zip_file_3(self):
        # The returned open file object provides the raw contents of the zip file
        path = self._make_zip()
        with open(path, "rb") as f:
            expected = f.read()
        zfp = ZipFileProcessor(path)
        file = zfp.read_zip_file()
        self.addCleanup(lambda: file.close() if file is not None else None)
        self.assertIsNotNone(file)
        self.assertEqual(file.read(), expected)

    def test_read_zip_file_4(self):
        # A file that does not exist: unsuccessful, so returns None
        missing = os.path.join(self.dir, "does_not_exist.zip")
        zfp = ZipFileProcessor(missing)
        self.assertIsNone(zfp.read_zip_file())

    def test_read_zip_file_5(self):
        # A file that exists but is not a valid zip file: unsuccessful, returns None
        path = os.path.join(self.dir, "not_a_zip.zip")
        with open(path, "w") as f:
            f.write("this is plain text, not a zip archive")
        zfp = ZipFileProcessor(path)
        self.assertIsNone(zfp.read_zip_file())

class AgentTest_extract_all(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.dir = self._tmp.name

    def _make_zip(self, name="aaa.zip", members=None):
        if members is None:
            members = {"bbb.txt": "hello"}
        path = os.path.join(self.dir, name)
        with zipfile.ZipFile(path, "w") as zf:
            for member_name, content in members.items():
                zf.writestr(member_name, content)
        return path

    def _make_output_dir(self, name="result"):
        out = os.path.join(self.dir, name)
        os.makedirs(out, exist_ok=True)
        return out

    def test_extract_all_1(self):
        # A valid zip file and an existing output path: extraction succeeds, returns True
        path = self._make_zip()
        out = self._make_output_dir()
        zfp = ZipFileProcessor(path)
        self.assertIs(zfp.extract_all(out), True)

    def test_extract_all_2(self):
        # The extracted file is placed in the output path with its original contents
        path = self._make_zip(members={"bbb.txt": "hello"})
        out = self._make_output_dir()
        zfp = ZipFileProcessor(path)
        zfp.extract_all(out)
        extracted = os.path.join(out, "bbb.txt")
        self.assertTrue(os.path.isfile(extracted))
        with open(extracted, "r") as f:
            self.assertEqual(f.read(), "hello")

    def test_extract_all_3(self):
        # Every file contained in the zip is extracted, not just one of them
        members = {
            "bbb.txt": "first file",
            "ccc.txt": "second file",
            "ddd.txt": "third file",
        }
        path = self._make_zip(members=members)
        out = self._make_output_dir()
        zfp = ZipFileProcessor(path)
        self.assertIs(zfp.extract_all(out), True)
        for member_name, content in members.items():
            extracted = os.path.join(out, member_name)
            self.assertTrue(os.path.isfile(extracted), member_name)
            with open(extracted, "r") as f:
                self.assertEqual(f.read(), content)

    def test_extract_all_4(self):
        # A zip file that does not exist: unsuccessful, returns False
        missing = os.path.join(self.dir, "does_not_exist.zip")
        out = self._make_output_dir()
        zfp = ZipFileProcessor(missing)
        self.assertIs(zfp.extract_all(out), False)

    def test_extract_all_5(self):
        # A file that exists but is not a valid zip archive: unsuccessful, returns False
        path = os.path.join(self.dir, "not_a_zip.zip")
        with open(path, "w") as f:
            f.write("this is plain text, not a zip archive")
        out = self._make_output_dir()
        zfp = ZipFileProcessor(path)
        self.assertIs(zfp.extract_all(out), False)

import os

import tempfile

import zipfile

class AgentTest_extract_file(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.dir = self._tmp.name

    def _make_zip(self, name="aaa.zip", members=None):
        if members is None:
            members = {"bbb.txt": "hello"}
        path = os.path.join(self.dir, name)
        with zipfile.ZipFile(path, "w") as zf:
            for member_name, content in members.items():
                zf.writestr(member_name, content)
        return path

    def _make_output_dir(self, name="result"):
        out = os.path.join(self.dir, name)
        os.makedirs(out, exist_ok=True)
        return out

    def test_extract_file_1(self):
        # A named file that exists in the zip, and an existing output path: returns True
        path = self._make_zip(members={"bbb.txt": "hello"})
        out = self._make_output_dir()
        zfp = ZipFileProcessor(path)
        self.assertIs(zfp.extract_file("bbb.txt", out), True)

    def test_extract_file_2(self):
        # The named file is placed in the output path with its original contents
        path = self._make_zip(members={"bbb.txt": "hello"})
        out = self._make_output_dir()
        zfp = ZipFileProcessor(path)
        zfp.extract_file("bbb.txt", out)
        extracted = os.path.join(out, "bbb.txt")
        self.assertTrue(os.path.isfile(extracted))
        with open(extracted, "r") as f:
            self.assertEqual(f.read(), "hello")

    def test_extract_file_3(self):
        # Only the file with the specified name is extracted, not the other members of the zip
        members = {
            "bbb.txt": "first file",
            "ccc.txt": "second file",
            "ddd.txt": "third file",
        }
        path = self._make_zip(members=members)
        out = self._make_output_dir()
        zfp = ZipFileProcessor(path)
        self.assertIs(zfp.extract_file("ccc.txt", out), True)
        extracted = os.path.join(out, "ccc.txt")
        self.assertTrue(os.path.isfile(extracted))
        with open(extracted, "r") as f:
            self.assertEqual(f.read(), "second file")
        self.assertFalse(os.path.exists(os.path.join(out, "bbb.txt")))
        self.assertFalse(os.path.exists(os.path.join(out, "ddd.txt")))

    def test_extract_file_4(self):
        # A file name that is not contained in the zip: unsuccessful, returns False
        path = self._make_zip(members={"bbb.txt": "hello"})
        out = self._make_output_dir()
        zfp = ZipFileProcessor(path)
        self.assertIs(zfp.extract_file("not_in_zip.txt", out), False)

    def test_extract_file_5(self):
        # A zip file that does not exist: unsuccessful, returns False
        missing = os.path.join(self.dir, "does_not_exist.zip")
        out = self._make_output_dir()
        zfp = ZipFileProcessor(missing)
        self.assertIs(zfp.extract_file("bbb.txt", out), False)

import os

import tempfile

import zipfile

class AgentTest_create_zip_file(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.dir = self._tmp.name

    def _make_source_files(self, members=None):
        if members is None:
            members = {"bbb.txt": "hello", "ccc.txt": "second file", "ddd.txt": "third file"}
        src_dir = os.path.join(self.dir, "src")
        os.makedirs(src_dir, exist_ok=True)
        paths = []
        for name, content in members.items():
            path = os.path.join(src_dir, name)
            with open(path, "w") as f:
                f.write(content)
            paths.append(path)
        return paths

    def _make_output_dir(self, name="output"):
        out = os.path.join(self.dir, name)
        os.makedirs(out, exist_ok=True)
        return out

    def test_create_zip_file_1(self):
        # Existing source files and an existing output location: compression succeeds, returns True
        files = self._make_source_files()
        out = os.path.join(self._make_output_dir(), "bcd")
        zfp = ZipFileProcessor(os.path.join(self.dir, "aaa.zip"))
        self.assertIs(zfp.create_zip_file(files, out), True)
        self.assertTrue(os.path.isfile(out))

    def test_create_zip_file_2(self):
        # The created file is a valid zip archive containing every listed file
        files = self._make_source_files()
        out = os.path.join(self._make_output_dir(), "bcd")
        zfp = ZipFileProcessor(os.path.join(self.dir, "aaa.zip"))
        zfp.create_zip_file(files, out)
        self.assertTrue(zipfile.is_zipfile(out))
        with zipfile.ZipFile(out, "r") as zf:
            names = {os.path.basename(n) for n in zf.namelist()}
        self.assertEqual(names, {"bbb.txt", "ccc.txt", "ddd.txt"})

    def test_create_zip_file_3(self):
        # The archived files keep their original contents
        members = {"bbb.txt": "hello", "ccc.txt": "second file"}
        files = self._make_source_files(members=members)
        out = os.path.join(self._make_output_dir(), "bcd")
        zfp = ZipFileProcessor(os.path.join(self.dir, "aaa.zip"))
        zfp.create_zip_file(files, out)
        with zipfile.ZipFile(out, "r") as zf:
            contents = {}
            for n in zf.namelist():
                contents[os.path.basename(n)] = zf.read(n).decode("utf-8")
        self.assertEqual(contents, members)

    def test_create_zip_file_4(self):
        # One of the listed files does not exist: unsuccessful, returns False
        files = self._make_source_files(members={"bbb.txt": "hello"})
        files.append(os.path.join(self.dir, "src", "missing.txt"))
        out = os.path.join(self._make_output_dir(), "bcd")
        zfp = ZipFileProcessor(os.path.join(self.dir, "aaa.zip"))
        self.assertIs(zfp.create_zip_file(files, out), False)

    def test_create_zip_file_5(self):
        # The archive contains only the listed files, not other files from the source directory
        files = self._make_source_files()
        extra_path = os.path.join(self.dir, "src", "extra.txt")
        with open(extra_path, "w") as f:
            f.write("not requested")
        selected = files[:2]
        out = os.path.join(self._make_output_dir(), "bcd")
        zfp = ZipFileProcessor(os.path.join(self.dir, "aaa.zip"))
        self.assertIs(zfp.create_zip_file(selected, out), True)
        with zipfile.ZipFile(out, "r") as zf:
            names = {os.path.basename(n) for n in zf.namelist()}
        self.assertEqual(names, {"bbb.txt", "ccc.txt"})
        self.assertNotIn("extra.txt", names)
        self.assertNotIn("ddd.txt", names)