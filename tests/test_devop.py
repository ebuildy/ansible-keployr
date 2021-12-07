import os
import tempfile
import subprocess

current_dir = os.getcwd()

def assert_files_equal(file1, file2):
    f1 = open(file1, "r")
    f2 = open(file2, "r")
    
    for line1, line2 in zip(f1, f2):
        assert line1 == line2
            
    assert True
    

def test_devop_makefile():
    with tempfile.TemporaryDirectory() as tmpDir:
        p = subprocess.Popen(f"ansible-playbook --extra-vars kp_build_dir={tmpDir} -t devop_build {current_dir}/makefile/playbook.yaml", shell=True, stdout=subprocess.PIPE)
        retval = p.wait()
        print(p.stdout.read())
        
        assert retval == 0
        
        assert_files_equal(f"{tmpDir}/Makefile", f"{current_dir}/makefile/snapshots/Makefile")
        assert_files_equal(f"{tmpDir}/README.MD", f"{current_dir}/makefile/snapshots/README.MD")
    

def test_devop_deploy():
    with tempfile.TemporaryDirectory() as tmpDir:
        p = subprocess.Popen(f"ansible-playbook --extra-vars kp_tmp_dir={tmpDir} -t git_deploy {current_dir}/git_deploy/playbook.yaml", shell=True, stdout=subprocess.PIPE)
        retval = p.wait()
        print(p.stdout.read())
        
        assert retval == 0