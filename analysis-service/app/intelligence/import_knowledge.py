

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
    },

    'VirtualAlloc': {
        'category': 'Memory Management',
        'description': 'Reserves or commits memory in the process address space.',
        'risk': 'Medium'
    },

    'VirtualAllocEx': {
        'category': 'Memory Management',
        'description': 'Reserves or commits memory in the address space of a specified process.',
        'risk': 'High'
    },

    'VirtualFree': {
        'category': 'Memory Management',
        'description': 'Releases or decommits memory allocated in the process address space.',
        'risk': 'Low'
    },

    'VirtualProtect': {
        'category': 'Memory Management',
        'description': 'Changes the access protection of a region of memory.',
        'risk': 'Medium'
    },

    'VirtualQuery': {
        'category': 'Memory Management',
        'description': 'Retrieves information about a region of virtual memory.',
        'risk': 'Low'
    },

    'HeapAlloc': {
        'category': 'Memory Management',
        'description': 'Allocates a block of memory from a process heap.',
        'risk': 'Low'
    },

    'HeapFree': {
        'category': 'Memory Management',
        'description': 'Releases a block of memory allocated from a process heap.',
        'risk': 'Low'
    },

    'CreateProcessA': {
        'category': 'Process Creation',
        'description': 'Creates a new process and its primary thread.',
        'risk': 'Medium'
    },

    'CreateProcessW': {
        'category': 'Process Creation',
        'description': 'Creates a new process and its primary thread using Unicode parameters.',
        'risk': 'Medium'
    },

    'OpenProcess': {
        'category': 'Process Access',
        'description': 'Opens an existing process and returns a handle with requested access rights.',
        'risk': 'Medium'
    },

    'TerminateProcess': {
        'category': 'Process Control',
        'description': 'Terminates a specified process.',
        'risk': 'Low'
    },

    'CreateThread': {
        'category': 'Thread Creation',
        'description': 'Creates a new thread within the current proccess',
        'risk': 'Low'
    },

    'CreateRemoteThread': {
        'category': 'Remote Thread Creation',
        'description': 'Creates a thread in the address space of another process.',
        'risk': 'High'
    },

    'WriteProcessMemory': {
        'category': 'Process Memory',
        'description': 'Writes data into the memory space of a specified process.',
        'risk': 'High'
    },

    'LoadLibraryA': {
        'category': 'Dynamic Loading',
        'description': 'Loads a DLL into the process.',
        'risk': 'Medium'
    },

    'LoadLibraryW': {
        'category': 'Dynamic Loading',
        'description': 'Loads a DLL into the process using Unicode parameters.',
        'risk': 'Medium'
    },

    'GetProcAddress': {
        'category': 'Dynamic Loading',
        'description': 'Retrieves the address of an exported function from a loaded module.',
        'risk': 'Medium'
    },

    'FreeLibrary': {
        'category': 'Dynamic Loading',
        'description': 'Decrements the reference count of a loaded DLL and unloads it when appropriate.',
        'risk': 'Low'
    },

    'createFileA': {
        'category': 'File System',
        'description': 'Creates or opens a file, device, or other I/O resource.',
        'risk': 'Low'
    },

    'CreateFileW': {
        'category': 'File System',
        'description': 'Create or opens a file, device, or other I/O resource using Unicode parameters.',
        'risk': 'Low'
    },

    'ReadFile': {
        'category': 'File System',
        'description': 'Reads data from a file or other input resource.',
        'risk': 'Low'
    },

    'WriteFile': {
        'category': 'File System',
        'description': 'Writes data to a file or other output resource.',
        'risk': 'Low'
    },

    'DeleteFileA': {
        'category': 'File System',
        'description': 'Deletes a specified file.',
        'risk': 'Low'
    },

    'DeleteFileW': {
        'category': 'File System',
        'description': 'Deletes a specified file using Unicode parameters.',
        'risk': 'Low'
    },

    'FindNextFileA': {
        'category': 'File Discovery',
        'description': 'Continues searching for files matching a specified pattern.',
        'risk': 'Low'
    },

    'RegOpenKeyExA': {
        'category': 'Registry',
        'description': 'Opens a specified registry key with requested access rights.',
        'risk': 'Medium'
    },

    'RegQueryValueExA': {
        'category': 'Registry',
        'description': 'Retrieves the data associated with a value in a registry key.',
        'risk': 'Medium'
    },

    'RegSetValueExA': {
        'category': 'Registry',
        'description': 'Sets the data and type of a specified registry value.',
        'risk': 'Medium'
    },

    'InternetOpenA': {
        'category': 'Networking',
        'description': 'Initializes access to Internet resources through the WinINet API.',
        'risk': 'Medium'
    },

    'InternetConnectA': {
        'category': 'Networking',
        'description': 'Establishes a connection to an Internet server using WinINet.',
        'risk': 'Medium'
    },

    'HttpOpenRequestA': {
        'category': 'Networking',
        'description': 'Creates an HTTP request handle for communication with an HTTP server.',
        'risk': 'Medium'
    },

    'WinHttpOpen': {
        'category': 'Networking',
        'description': 'Initializes use of the Windows HTTP Services API.',
        'risk': 'Medium'
    },

    'WinHttpConnect': {
        'category': 'Networking',
        'description': 'Establishes a connection to an HTTP server using Windows HTTP Services.',
        'risk': 'Medium'
    }
}