## task: git deploy

Deploy built artifacts (git clone, commit & push) to a git repository used as gitops source (via argocd).

The repository must respect this file structure:

```
env_dev
    stack1
        gitops_apps
        service1
env_prod
    stack1
        gitops_apps
        service1
```

1 cluster = 1 env

## task: devop_build

This task will build a Makefile , a README.md according:

### Variables

```
kp_devop:
    envs:
    -   name: dev
        dns_suffix: ".cluster-dev.X.ca"
        vars_file: ca1_dev.yaml
    -   name: prod
        dns_suffix: ".cluster-prod.X.ca"
        vars_file: ca1_prod.yaml
    actions:
    -   name: Clean
        tags: clean
    -   name: build
        actions:
        - zeppelin.build
        - djobi.pipelines
        - argocd_apps.build
    services:
    -   name: devop
        actions:
        -   name: makefile
            tags: devop_build,makefile
        -   name: deploy
            tags: git_deploy
    -   name: zeppelin
        actions:
        -   name: build
            tags: zeppelin,server
        urls:
        -   ingress: zep
    -   name: argocd_apps
        actions:
        -   name: build
            tags: argocd_apps
```