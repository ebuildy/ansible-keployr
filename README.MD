# Installation

## Ansible Galaxy

https://galaxy.ansible.com/ebuildy/keployr

```
ansible-galaxy collection install ebuildy.keployr
```

## Docker

See https://github.com/ebuildy/docker-ansible-keployr project.

# Roles

## Role: app

```
- name: Helm chart
  include_role:
    name: ebuildy.keployr.app
    apply: { tags: ["always"] }
  tags: ["always"]
  vars:
    keployr_argocd_enabled: true
    keployr_build_as_manifests: false
    keployr_helm_values:
      zeppelin:
        ....
    keployr_helm_charts:
    - name: zeppelin
      repository: "{{ data_lake_helm_repo }}"
      version: 0.2.0
```

### Create argoCD app of apps / applicationSet

```
-   name: ArgoCD app of apps
    include_role:
        name: ebuildy.keployr.app
        tasks_from: argocd_appset
```

## Role: devop

````
tasks:
-   name: Deploy to git-ops repository
    include_role:
    name: ebuildy.keployr.devop
    vars:
        keployr_git_branch: master
        keployr_git_deploy_src_fullpath: "{{ build_dir }}"
        keployr_git_deploy_dst_path: "{{ env_name }}/{{ keployr_stack }}"
    tags: ["never", "git_deploy"]
-   name: Generate makefile and readme
    include_role:
    name: ebuildy.keployr.devop
    vars: {}
    tags: ["never", "devop_build"]
```