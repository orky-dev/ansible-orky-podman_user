A simple Ansible role to create user for running Podman rootless containers.

This role using the same subordinate id ranges as [FreeIPA](https://freeipa.readthedocs.io/en/latest/designs/subordinate-ids.html#revision-1-limitation).

## Vars
```yaml
podman_user: kek
podman_group: "{{ podman_user }}"
```

## Usage
1. Create 3 .yml files
    ```bash
    ├── inventory.yml
    ├── playbook.yml
    └── requirements.yml
    ```

2. Add to `requirements.yml`

    ```yaml
    ---
    roles:
      - name: orky.podman_user
        src: ssh://git@github.com/orky-dev/ansible-orky-podman_user.git
        version: v0.3.1
        scm: git
    ```

3. Install the role

    ```yaml
    ansible-galaxy install -r requirements.yml
    ```

4. Add to `playbook.yml`

    ```yaml
    - hosts: podman_servers
      roles:
        - role: orky.podman_user
          podman_user: kek
          become: yes
    ```
5. Update `inventory.yml` using your credentials and hosts

    ```yaml
    ---
    podman_servers:
      hosts:
        my_podman_host_number_one:
          ansible_host: x.x.x.x
          ansible_user: root
    ```

6. Run playbook
    ```yaml
    ansible-playbook -i inventory.yml playbook.yml
    ```

### TODO:
1. ~~Rewrite generation of subuid/subgid~~
2. Python code to test all subuid/subgid ranges for overlapping. 
3. Add generation of subuids for more than one user. Ofc you can run the role in for-loop but it is going to be ineffective for a lot of users, might be the problem at thousands, but it is okay for tens or hundreds.
4. Add CI and simple role tests.
