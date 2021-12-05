galaxy/build:
	ansible-galaxy collection build --force

galaxy/publish:
	ansible-galaxy collection publish $(ANSIBLE_FILE) --token $(ANSIBLE_TOKEN)