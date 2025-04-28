# Custom Encoding Mappings

# Category priority encoding
category_priority = {
    'Collection': 1,
    'CommandAndControl': 2,
    'CredentialAccess': 1,
    'CredentialStealing': 0,
    'DefenseEvasion': 1,
    'Discovery': 1,
    'Execution': 1,
    'Exfiltration': 2,
    'Exploit': 1,
    'Impact': 1,
    'InitialAccess': 1,
    'LateralMovement': 2,
    'Malware': 2,
    'Persistence': 2,
    'PrivilegeEscalation': 2,
    'Ransomware': 2,
    'SuspiciousActivity': 1,
    'UnwantedSoftware': 2,
    'Weaponization': 3,
    'WebExploit': 2
}

# IncidentGrade encoding
incident_grade_mapping = {
    'TruePositive': 2,
    'BenignPositive': 1,
    'FalsePositive': 0
}

# Entity encoding
entity_priority = {
    'ActiveDirectoryDomain': 0,
    'AmazonResource': 2,
    'AzureResource': 2,
    'Blob': 0,
    'BlobContainer': 0,
    'CloudApplication': 1,
    'CloudLogonRequest': 3,
    'CloudLogonSession': 1,
    'Container': 1,
    'ContainerImage': 1,
    'ContainerRegistry': 1,
    'File': 2,
    'GenericEntity': 2,
    'GoogleCloudResource': 0,
    'IoTDevice': 3,
    'Ip': 1,
    'KubernetesCluster': 1,
    'KubernetesNamespace': 1,
    'KubernetesPod': 1,
    'Machine': 1,
    'MailCluster': 1,
    'MailMessage': 2,
    'Mailbox': 1,
    'MailboxConfiguration': 1,
    'Malware': 1,
    'Nic': 3,
    'OAuthApplication': 1,
    'Process': 2,
    'RegistryKey': 0,
    'RegistryValue': 0,
    'SecurityGroup': 0,
    'Url': 2,
    'User': 1
}

# === Encoding Functions ===

def encode_category(df, column_name='Category'):
    """
    Encode the Category column using custom priority mapping.
    """
    df['Category_encoded'] = df[column_name].map(category_priority).fillna(0).astype(int)
    return df

def encode_incident_grade(df, column_name='IncidentGrade'):
    """
    Encode the IncidentGrade column using custom mapping.
    """
    df['IncidentGrade_encoded'] = df[column_name].map(incident_grade_mapping).fillna(0).astype(int)
    return df

def encode_entity(df, column_name='EntityType'):
    """
    Encode the EntityType column using custom entity priority mapping.
    """
    df['Entity_encoded'] = df[column_name].map(entity_priority).fillna(0).astype(int)
    return df
