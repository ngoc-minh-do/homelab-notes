# Create Proxmox API Token

1. Navigate to the Proxmox portal, click on `Datacenter > Permissions > Groups`
2. Click the Create button. Name the group something informative, like `api-ro-users`
3. Click on the `Permissions > Add -> Group Permission`

        Path: /
        Group: group from Step 2
        Role: PVEAuditor
        Propagate: Checked
    
4. Click on the `Permissions > Users > Add`

        User name: something informative like api
        Realm: Linux PAM standard authentication
        Group: group from Step 2
    
5. Click on the `Permissions > API Tokens > Add`

        User: user from Step 4
        Token ID: something informative like the application or purpose like homepage
        Privilege Separation: Checked
    
6. Click on the `Permissions > Add > API Token Permission`

        Path: /
        API Token: select the Token ID created in Step 5
        Role: PVE Auditor
        Propagate: Checked
    