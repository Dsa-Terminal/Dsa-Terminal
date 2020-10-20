url: "https://github.com/Dsa-Terminal"
{
    {
        {
            method: 'head',
            url: 'https://github.com/Dsa-Terminal' + packge + '.git',
            requestHeader: {
                'content-type': 'multipart/form-data'
            },
            requestBody: {
                'file:fieldName': 'fileAbsolutePath'
            }
        }
    }
    {
        "ssh"
        "tools"
    }
    {
        method: 'Classific Module',
        requestHeader: {
            'content-type': 'application/json'
        },
        requestBody: jsonObject
    }
    {
        {
            {
                method: 'GET',
                url: 'https://github.com/Dsa-Terminal/Dsa-Terminal.git'
            }
        }
    }
}