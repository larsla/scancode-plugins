A ScanCode scan plugin to get lkmclue, dwarf, gwt, cpp includes, code/comments lines generated code and elf info.

--cpp-includes: 
--dwarf: 
--elf: 
--generatedcode:
--gwt:
--javaclass:
--makedepend:
--codecommentlines:

To start the test case, please run:
1. ./configure
2. source bin/activate
3. pip install -e plugins/scancode-dwarfdump-manylinux2014_x86_64  -e plugins/scancode-ctags-manylinux2014_x86_64 -e plugins/scancode-readelf-manylinux2014_x86_64 -e plugins/scancode-compiledcode
4. pytest -vvs plugins/scancode-compiledcode/tests/test_lkmclue.py
   pytest -vvs plugins/scancode-compiledcode/tests/test_elf.py
   pytest -vvs plugins/scancode-compiledcode/tests/test_cpp_includes.py
   pytest -vvs plugins/scancode-compiledcode/tests/test_dwarf.py
   pytest -vvs plugins/scancode-compiledcode/tests/test_gwt.py
   pytest -vvs plugins/scancode-compiledcode/tests/test_makedepend.py
   pytest -vvs plugins/scancode-compiledcode/tests/test_javaclass.py
   pytest -vvs plugins/scancode-compiledcode/tests/test_generatedcode.py
   pytest -vvs plugins/scancode-compiledcode/tests/test_sourcecode.py
   pytest -vvs plugins/scancode-compiledcode/tests/test_dwarf.py
   pytest -vvs plugins/scancode-compiledcode/tests/test_dwarf2.py
   pytest -vvs plugins/scancode-compiledcode/tests/test_dwarf3.py


Note that in step3, the path depends on your OS versions, please update according to your real os enviroment.