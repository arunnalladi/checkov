// pass

resource enabled 'Microsoft.ContainerService/managedClusters@2022-08-03-preview' = {
  name: 'string'
  location: resourceGroup().location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    enableRBAC: true
    agentPoolProfiles: [
      {
        name: 'agentpool'
        osDiskSizeGB: osDiskSizeGB
        osSKU: 'Ubuntu'
        osType: 'Linux'
      }
    ]
    addonProfiles: {
      omsagent: {
        config: {
          logAnalyticsWorkspaceResourceID: logAnalyticsWorkspace.id
        }
        enabled: true
      }
      kubeDashboard: {
        enabled: false
      }
    }
    apiServerAccessProfile: {
      authorizedIPRanges: [
        '10.0.0.0/8'
      ]
    }
    networkProfile: {
      networkPlugin: 'azure'
      networkPolicy: 'azure'
    }
    linuxProfile: {
      adminUsername: linuxAdminUsername
      ssh: {
        publicKeys: [
          {
            keyData: sshRSAPublicKey
          }
        ]
      }
    }
  }
}

resource enabledCamelCase 'Microsoft.ContainerService/managedClusters@2022-08-03-preview' = {
  name: 'string'
  location: resourceGroup().location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    enableRBAC: true
    agentPoolProfiles: [
      {
        name: 'agentpool'
        osDiskSizeGB: osDiskSizeGB
        osSKU: 'Ubuntu'
        osType: 'Linux'
      }
    ]
    addonProfiles: {
      omsAgent: {
        config: {
          logAnalyticsWorkspaceResourceID: logAnalyticsWorkspace.id
        }
        enabled: true
      }
      kubeDashboard: {
        enabled: false
      }
    }
    apiServerAccessProfile: {
      authorizedIPRanges: [
        '10.0.0.0/8'
      ]
    }
    networkProfile: {
      networkPlugin: 'azure'
      networkPolicy: 'azure'
    }
    linuxProfile: {
      adminUsername: linuxAdminUsername
      ssh: {
        publicKeys: [
          {
            keyData: sshRSAPublicKey
          }
        ]
      }
    }
  }
}

// fail

resource default 'Microsoft.ContainerService/managedClusters@2022-08-03-preview' = {
  name: 'string'
  location: resourceGroup().location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    agentPoolProfiles: [
      {
        name: 'agentpool'
        osDiskSizeGB: osDiskSizeGB
        osSKU: 'Ubuntu'
        osType: 'Linux'
      }
    ]
    addonProfiles: {
      kubeDashboard: {
        enabled: false
      }
    }
    apiServerAccessProfile: {
      disableRunCommand: true
    }
    networkProfile: {
      networkPlugin: 'azure'
      networkPolicy: 'azure'
    }
    linuxProfile: {
      adminUsername: linuxAdminUsername
      ssh: {
        publicKeys: [
          {
            keyData: sshRSAPublicKey
          }
        ]
      }
    }
  }
}
