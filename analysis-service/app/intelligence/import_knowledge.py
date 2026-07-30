

IMPORT_KNOWLEDGE = {

    'VirtualProtect': {
        'category': 'Memory Management',
        'description': 'Changes memory protection attributes',
        'risk': 'Medium'
    },

    'VirtualQuery': {
        'category': 'Memory Management',
        'description': 'Retrieves information about memory regions.',
        'risk': 'Low'
    },

    'LoadLibraryA': {
        'category': 'Dynamic Loading',
        'description': 'Loads a DLL into the process.',
        'risk': 'Medium'
    },

    'GetProcAddress': {
        'category': 'Dynamic Loading',
        'description': 'Retrieves the address of an exported function.',
        'risk': 'Medium'
    },

    'FindFirstFileA': {
        'category': 'File Discovery',
        'description': 'Searches for files matching a pattern.',
        'risk': 'Low'
    }
}