# Nextcloud

## Issue

1. WebUI's Overview show

        One or more mimetype migrations are available. Occasionally new mimetypes are added to better handle certain file types. Migrating the mimetypes take a long time on larger instances so this is not done automatically during upgrades. Use the command `occ maintenance:repair --include-expensive` to perform the migrations.

    On `nextcloud-aio-nextcloud` container, run:

            sudo -u www-data php occ maintenance:repair --include-expensive

2. WebUI's Logging show `"xxx" is locked, existing lock on file: exclusive"`

    On `nextcloud-aio-nextcloud` container, get db's information from `config/config.php`, then run:

        psql -h <server> -U <user> -d <database>
        DELETE FROM oc_file_locks WHERE true 

    Then, run:

        sudo -u www-data php occ files:scan --all