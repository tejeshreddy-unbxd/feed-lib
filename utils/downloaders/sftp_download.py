import pysftp
import os

class DownloadFileFromSFTP():
    def __init__(self, sftp_download_config):
        with pysftp.Connection(sftp_download_config['hostname'], username=sftp_download_config['username'], password=sftp_download_config['password']) as sftp:
            print(sftp.listdir())
            
            in_path = os.path.join(sftp_download_config['input_dir'], sftp_download_config['input_file'])
            out_path = os.path.join(sftp_download_config['root_dir'], sftp_download_config['mnt_folder'], sftp_download_config['output_dir'], sftp_download_config['output_file'])
            
            os.chdir(out_path)
            sftp.get(in_path)
            #sftp.cd(self.sftp_download_config['input_dir'])
        

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

x = DownloadFileFromSFTP(sftp_download_config)