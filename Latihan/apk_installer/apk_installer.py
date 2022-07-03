#pylint:disable=W0612
#pylint:disable=W0611
import sys, os
from pyaxmlparser import APK
from zipfile import ZipFile
from pathlib import Path
from glob import glob

TEMPDIR = "/storage/emulated/0/.temp/apk_installer/"
DATADIR = "/data/app/"
def echo(xyz):
	print(f'-- {xyz}')
def clear_temp():
	os.system(f'rm -f {TEMPDIR}*')

def main():
	os.system('clear')
	if not os.path.exists(TEMPDIR):
		os.mkdir(TEMPDIR)
	if sys.argv[1] == '--apks':
		is_apks = True
	else:
		is_apks = False
	if is_apks:
		echo('extract split apk')
		with ZipFile(sys.argv[2], 'r') as open_apks:
			open_apks.extractall(TEMPDIR)
		split_apk = glob(f'{TEMPDIR}split_*')
		
		apk = APK(f'{TEMPDIR}base.apk')
		
		pkg_dir = (f'{DATADIR}{apk.package}-1')
		echo('installing apk')
		os.system(f'su -c pm install -r {TEMPDIR}base.apk')
		echo('installing split apk')
		for i in range(0, len(split_apk), 1):
			split = split_apk[i]
			os.system(f'su -c busybox cp -v {split} {pkg_dir}')
		echo('set permision')
		os.system(f'su -c chmod 644 {pkg_dir}/split*apk')
		echo('extract library')
		
		os.system(f'su -c [ ! -d {pkg_dir}/lib/arm ] && mkdir -p {pkg_dir}/lib/arm')
		for i in range(0, len(split_apk)):
			with ZipFile(split_apk[i], 'r') as whatever:
				list_file = whatever.namelist()
				if 'lib/' in list_file:
					 lib = split_apk[i]
					 os.system(f"su -c [ -d {pkg_dir}/lib/arm ] && unzip {lib} -d {pkg_dir}/lib/arm")
					 break
		
		echo('set library permision')
		os.system(f'su -c chmod -R 755 {pkg_dir}/lib')
		echo('installation finish')
		clear_temp()
if __name__ == '__main__':
	main()

