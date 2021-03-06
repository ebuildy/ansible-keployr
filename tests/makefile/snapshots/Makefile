##
# Generated by keployr
##

# Default ansible playbook file
KEPLOYR_FILE ?= "./src/keployr.yaml"

# Default ansible tags
KEPLOYR_TAGS ?= ""

# Default env name
KEPLOYR_ENV ?= dev

comma:= ,

define keployr_fn
	ansible-playbook ${KEPLOYR_FILE} --tags=$(1) -i localhost,
endef

###
# open URL
###
.PHONY: keployr/dev/zeppelin/url-zep
keployr/dev/zeppelin/url-zep:
	@echo "https://zep.dev.cluster.infra"
	open "https://zep.dev.cluster.infra"

.PHONY: keployr/prod/zeppelin/url-zep
keployr/prod/zeppelin/url-zep:
	@echo "https://zep.prod.cluster.infra"
	open "https://zep.prod.cluster.infra"


###
# main actions
###
.PHONY: keployr/clean
keployr/clean: 
	$(call keployr_fn,"clean")

.PHONY: keployr/build
keployr/build: keployr/svc/zeppelin/build keployr/svc/argocd_apps/build 


###
# services
###
.PHONY: keployr/svc/devop/makefile
keployr/svc/devop/makefile:
	$(call keployr_fn,"devop_build$(comma)makefile")

.PHONY: keployr/svc/devop/deploy
keployr/svc/devop/deploy:
	$(call keployr_fn,"git_deploy")


.PHONY: keployr/svc/zeppelin/build
keployr/svc/zeppelin/build:
	$(call keployr_fn,"zeppelin$(comma)server")


.PHONY: keployr/svc/argocd_apps/build
keployr/svc/argocd_apps/build:
	$(call keployr_fn,"argocd_apps")



###
# utils
###

print/env:
	printenv | grep KEPLOYR

CIDRE_PLAYBOOK_FILE ?= ./ci/playbook.yaml

ci/build-makefile-readme:
	${KEPLOYR_BIN} devop_build

define call_cidre
    ansible-playbook ${CIDRE_PLAYBOOK_FILE} --tags $(1)
endef

cidre/bump/patch:
	$(call call_cidre,cidre_bump_patch)

cidre/bump/minor:
	$(call call_cidre,cidre_bump_minor)

cidre/bump/major:
	$(call call_cidre,cidre_bump_major)

cidre/ms_close:
	$(call call_cidre,cidre_ms_close)
