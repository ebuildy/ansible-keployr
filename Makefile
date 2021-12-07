galaxy/build:
	ansible-galaxy collection build --force

galaxy/publish:
	ansible-galaxy collection publish $(ANSIBLE_FILE) --token $(ANSIBLE_TOKEN)

test/snapshot/devop/makefile:
	mkdir -p $$PWD/tests/makefile/snapshots
	rm -rf $$PWD/tests/makefile/snapshots/*
	ansible-playbook -t devop_build --extra-vars kp_devop_build_dir=$$PWD/tests/makefile/snapshots ./tests/makefile/playbook.yaml