'''
    - name the transformr based on the client
'''

name_transformer = {
    'Image Src': {
        'name': 'imageUrl',
        'persist': False,
        'type': str,
        'include': True 
    },
    'Title': {
        'name': 'title',
        'persist': False,
        'type': str,
        'include': True 
    },
    'Variant SKU': {
        'name': 'uniqueId',
        'persist': False,
        'type': str,
        'include': True 
    }
}

''' 
    - SFTP download config
'''

sftp_download_config = {
    'hostname': 'sftp.unbxdapi.com',
    'username': 'perryellis',
    'password': '9b9rMhR8',
    'input_dir': '',
    'input_file': 'cubavera_published_products_and_variants.csv',
    'root_dir': '/mnt',
    'output_dir': '',
    'output_file': '',
    'mnt_folder': 'cubavera'
}
