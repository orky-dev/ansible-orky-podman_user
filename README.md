A simple Ansible role to create user for running Podman rootless containers.

This role using the same subordinate id ranges as FreeIPA.
https://freeipa.readthedocs.io/en/latest/designs/subordinate-ids.html#revision-1-limitation

## Vars
```yaml
podman_user: kek
podman_group: "{{ podman_user }}"
```

## Usage

1. Add to your `requirements.yml`, latest version is published as `tag` like `v0.3.1`

    ```yaml
    ---
    roles:
      - name: orky.podman_user
        src: ssh://git@github.com/orky-dev/ansible-orky-podman_user.git
        version: v0.3.1
        scm: git
    ```

2. Install the role

    ```yaml
    ansible-galaxy install -r requirements.yml
    ```

3. Then create the similar `playbook.yml`

    ```yaml
    - hosts: podman_servers
      roles:
        - role: orky.podman_user
          podman_user: kek
          become: yes
    ```
4. Also don't forget about `inventory.yml`

    ```yaml
    ---
    podman_servers:
      hosts:
        my_podman_host_number_one:
          ansible_host: x.x.x.x
          ansible_user: root
    ```
5. Your project directory gonna look like this
    ```bash
    ├── inventory.yml
    ├── playbook.yml
    └── requirements.yml
    ```

6. Run  playbook as simple as
    ```yaml
    ansible-playbook -i inventory.yml playbook.yml
    ```

### TODO:
1. ~~Rewrite generation of subuid/subgid~~
2. Python code to test all subuid/subgid ranges for overlapping. 
3. Add generation of subuids for more than one user (you can run the role for every user but it is going to be ineffective for a lot of users, might be the problems at hundreds of thousands, but it is okay for tens)
